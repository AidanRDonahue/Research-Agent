#!/usr/bin/env python3
"""Validate and deterministically package the Research-Agent Skill distribution."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"
MANIFEST_FILE = ROOT / "skills-manifest.json"
SKILLS_DIR = ROOT / "skills"
MAX_SKILL_ZIP_BYTES = 25 * 1024 * 1024
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def die(message: str) -> None:
    raise SystemExit(f"error: {message}")


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        die(f"cannot read valid JSON from {path}: {exc}")


def get_source_commit(explicit: str | None) -> str:
    candidates = [explicit, os.environ.get("GITHUB_SHA")]
    for candidate in candidates:
        if candidate and SHA40.fullmatch(candidate.lower()):
            return candidate.lower()
    try:
        candidate = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip().lower()
    except (OSError, subprocess.CalledProcessError):
        candidate = ""
    if SHA40.fullmatch(candidate):
        return candidate
    die("source commit is unavailable; run inside a Git checkout or pass --source-commit <40-hex-sha>")


def parse_skill_frontmatter(skill_md: Path) -> tuple[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        die(f"{skill_md} must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        die(f"{skill_md} has unterminated YAML frontmatter")
    frontmatter = text[4:end]
    name_match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.MULTILINE)
    description_match = re.search(r"^description:\s*(\S.*)$", frontmatter, re.MULTILINE)
    if not name_match or not description_match:
        die(f"{skill_md} frontmatter must contain non-empty name and description fields")
    return name_match.group(1), description_match.group(1).strip()


def validate_skill(name: str, path: Path) -> None:
    if not path.is_dir():
        die(f"manifest Skill path does not exist: {path}")
    skill_md = path / "SKILL.md"
    openai_yaml = path / "agents" / "openai.yaml"
    if not skill_md.is_file():
        die(f"{name} is missing SKILL.md")
    if not openai_yaml.is_file():
        die(f"{name} is missing agents/openai.yaml")
    declared_name, _ = parse_skill_frontmatter(skill_md)
    if declared_name != name:
        die(f"{skill_md} declares name {declared_name!r}, expected {name!r}")
    display_text = openai_yaml.read_text(encoding="utf-8")
    if not re.search(r"^\s*display_name:\s*\S", display_text, re.MULTILINE):
        die(f"{openai_yaml} must contain interface.display_name metadata")
    entrypoints = sorted(p.relative_to(path).as_posix() for p in path.rglob("SKILL.md"))
    if entrypoints != ["SKILL.md"]:
        die(f"{name} must contain exactly one SKILL.md entrypoint; found {entrypoints}")
    if (path / "DISTRIBUTION.json").exists():
        die(f"{name}/DISTRIBUTION.json is generated during packaging and must not be committed")
    for item in path.rglob("*"):
        if item.is_symlink():
            die(f"Skill packages may not contain symlinks: {item}")


def zip_info(arcname: str, executable: bool = False) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(arcname, FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = ((0o755 if executable else 0o644) & 0xFFFF) << 16
    return info


def write_zip_bytes(zf: zipfile.ZipFile, arcname: str, data: bytes, executable: bool = False) -> None:
    zf.writestr(zip_info(arcname, executable), data)


def package_skill(name: str, path: Path, destination: Path, metadata: dict) -> tuple[str, int]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for file_path in sorted(p for p in path.rglob("*") if p.is_file()):
            relative = file_path.relative_to(path).as_posix()
            arcname = f"{name}/{relative}"
            executable = bool(file_path.stat().st_mode & 0o111)
            write_zip_bytes(zf, arcname, file_path.read_bytes(), executable)
        generated = json.dumps(metadata, indent=2, sort_keys=True).encode("utf-8") + b"\n"
        write_zip_bytes(zf, f"{name}/DISTRIBUTION.json", generated)
    size = destination.stat().st_size
    if size > MAX_SKILL_ZIP_BYTES:
        die(f"{name} package is {size} bytes, exceeding the 25 MB Skill upload limit")
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    return digest, size


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "dist"), help="output directory (default: dist)")
    parser.add_argument("--source-commit", help="40-character source commit SHA; inferred from Git when omitted")
    args = parser.parse_args()

    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(version):
        die(f"VERSION must contain a semantic version, found {version!r}")
    manifest = load_json(MANIFEST_FILE)
    if manifest.get("schema_version") != 1:
        die("skills-manifest.json schema_version must be 1")
    if manifest.get("version") != version:
        die("VERSION and skills-manifest.json version do not match")
    if manifest.get("release_tag") != f"v{version}":
        die("skills-manifest.json release_tag must equal v<VERSION>")

    skill_entries = manifest.get("skills")
    if not isinstance(skill_entries, list) or not skill_entries:
        die("skills-manifest.json must contain a non-empty skills list")
    manifest_names = [entry.get("name") for entry in skill_entries]
    if len(manifest_names) != len(set(manifest_names)):
        die("skills-manifest.json contains duplicate Skill names")

    discovered = sorted(
        p.name for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
    )
    if sorted(manifest_names) != discovered:
        die(f"manifest Skill set {sorted(manifest_names)} does not match source Skill set {discovered}")

    source_commit = get_source_commit(args.source_commit)
    output = Path(args.output).resolve()
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    release_skills = []
    for entry in skill_entries:
        name = entry.get("name")
        relative_path = entry.get("path")
        if not isinstance(name, str) or not isinstance(relative_path, str):
            die("every manifest Skill entry must contain string name and path fields")
        path = ROOT / relative_path
        validate_skill(name, path)
        skill_metadata = {
            "schema_version": 1,
            "distribution": manifest["name"],
            "version": version,
            "release_tag": manifest["release_tag"],
            "source_repository": manifest["repository"],
            "source_commit": source_commit,
            "skill": name,
        }
        archive = output / name / "skill.zip"
        digest, size = package_skill(name, path, archive, skill_metadata)
        release_skills.append(
            {
                "name": name,
                "archive": f"{name}/skill.zip",
                "sha256": digest,
                "bytes": size,
            }
        )

    release_manifest = {
        "schema_version": 1,
        "distribution": manifest["name"],
        "version": version,
        "release_tag": manifest["release_tag"],
        "source_repository": manifest["repository"],
        "source_commit": source_commit,
        "project_lock": manifest["project_lock"],
        "skills": release_skills,
    }
    release_manifest_path = output / "research-agent-distribution.json"
    release_manifest_path.write_text(
        json.dumps(release_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    bundle = output / f"research-agent-skills-v{version}.zip"
    with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        write_zip_bytes(
            zf,
            "research-agent-distribution.json",
            release_manifest_path.read_bytes(),
        )
        for skill in release_skills:
            archive = output / skill["archive"]
            write_zip_bytes(zf, skill["archive"], archive.read_bytes())

    checksum_targets = [release_manifest_path, bundle] + [output / s["archive"] for s in release_skills]
    checksum_lines = []
    for target in checksum_targets:
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        checksum_lines.append(f"{digest}  {target.relative_to(output).as_posix()}")
    (output / "SHA256SUMS").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")

    print(f"validated and packaged {len(release_skills)} Skills for Research-Agent v{version}")
    print(f"source commit: {source_commit}")
    print(f"bundle: {bundle}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
