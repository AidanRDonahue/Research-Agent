#!/usr/bin/env python3
"""Compare a project's Research-Agent lock with a packaged distribution manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


def load(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"error: cannot read valid JSON from {path}: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("lock", help="path to research-agent.lock.json")
    parser.add_argument(
        "--distribution",
        required=True,
        help="path to research-agent-distribution.json from the installed/downloaded release",
    )
    args = parser.parse_args()

    lock_path = Path(args.lock)
    dist_path = Path(args.distribution)
    lock = load(lock_path)
    dist = load(dist_path)
    failures: list[str] = []

    if lock.get("schema_version") != 1:
        failures.append("project lock schema_version is not 1")
    if dist.get("schema_version") != 1:
        failures.append("distribution manifest schema_version is not 1")

    expected = lock.get("distribution")
    if not isinstance(expected, dict):
        failures.append("project lock is missing the distribution object")
        expected = {}

    comparisons = {
        "repository": (expected.get("repository"), dist.get("source_repository")),
        "version": (expected.get("version"), dist.get("version")),
        "release_tag": (expected.get("release_tag"), dist.get("release_tag")),
        "source_commit": (expected.get("source_commit"), dist.get("source_commit")),
    }
    for field, (wanted, actual) in comparisons.items():
        if not isinstance(wanted, str) or not wanted or wanted.startswith("<"):
            failures.append(f"project lock has no concrete {field}")
        elif wanted != actual:
            failures.append(f"{field} mismatch: project pins {wanted!r}, distribution is {actual!r}")

    required = lock.get("required_skills")
    if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
        failures.append("project lock required_skills must be a list of Skill names")
        required = []
    available = {
        item.get("name") for item in dist.get("skills", []) if isinstance(item, dict) and isinstance(item.get("name"), str)
    }
    missing = sorted(set(required) - available)
    if missing:
        failures.append(f"distribution is missing required Skills: {', '.join(missing)}")

    if failures:
        print("INCOMPATIBLE")
        for failure in failures:
            print(f"- {failure}")
        return 2

    print(
        f"COMPATIBLE: project pins Research-Agent {expected['version']} "
        f"at {expected['source_commit']} with {len(required)} required Skills"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
