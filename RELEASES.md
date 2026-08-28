# Research-Agent Releases

Research-Agent is distributed as a versioned agent-and-Skills toolchain. The source repository remains the development authority; tagged releases provide reproducible packages for installation into ChatGPT and for pinning in research projects.

## Release contract

A release is identified by the semantic version in `VERSION` and the matching tag `v<VERSION>`. `skills-manifest.json` lists the complete core Skill set for that release. `scripts/package_skills.py` validates that the manifest and source tree agree and then creates one independent `skill.zip` per Skill.

The packaging script also generates `research-agent-distribution.json`. Unlike the static source manifest, the generated distribution manifest records the exact Git commit used to build the packages. This avoids a circular attempt to hard-code a commit SHA into the commit that contains the manifest.

Each packaged Skill receives a generated `DISTRIBUTION.json` containing its distribution version, release tag, source repository, source commit, and Skill name. Do not commit generated `DISTRIBUTION.json` files into `skills/`.

The release bundle `research-agent-skills-v<VERSION>.zip` is only a transport bundle. It contains independent `<skill-name>/skill.zip` packages plus the generated distribution manifest. The bundle is **not** itself a ChatGPT Skill and must not be uploaded as though it were one.

## Semantic versioning

Use the repository-wide version as the compatibility version for the Agent and core Skill suite:

- **patch**: backward-compatible corrections, wording fixes, or packaging/validation fixes that do not intentionally change workflow contracts;
- **minor**: backward-compatible new Skills, new optional workflow capabilities, or meaningful procedural improvements;
- **major**: changes that intentionally break project compatibility, change authority boundaries, or require projects to migrate their stored workflow conventions.

A Skill may change internally without an individual version field. The release version identifies the tested suite as a whole.

## Preparing a release

1. Start from current `main` and create a scoped branch.
2. Make the Agent, Skill, packaging, documentation, or template changes.
3. Choose the next semantic version and update both `VERSION` and the `version` / `release_tag` fields in `skills-manifest.json`.
4. If the core Skill set changed, update the `skills` list in `skills-manifest.json` and relevant documentation/templates.
5. Run `python scripts/package_skills.py --output dist` locally when a Git checkout and Python 3 are available.
6. Open a pull request and require the `Validate and package Research-Agent Skills` workflow to pass.
7. Merge the reviewed change.
8. Create and push the tag `v<VERSION>` on the exact intended `main` commit.
9. The tag-triggered workflow validates the tag, rebuilds the packages from that commit, and publishes or refreshes the GitHub Release with the bundle, distribution manifest, and checksums.

Do not tag an unreviewed branch merely to obtain packages. Pull-request CI already produces an artifact for inspection.

## Project compatibility pins

An instantiated research project may store `research-agent.lock.json`. The lock is toolchain metadata, not research state and not a replacement for project-local `AGENTS.md`.

A concrete lock records:

- source repository;
- release version;
- release tag;
- exact source commit from `research-agent-distribution.json`; and
- the Skills that project expects to be available.

To check a project against a downloaded distribution manifest:

```bash
python scripts/check_project_compatibility.py \
  /path/to/project/research-agent.lock.json \
  --distribution /path/to/research-agent-distribution.json
```

A mismatch should trigger an explicit compatibility review. Do not silently rewrite the project lock just because a newer Research-Agent release exists.
