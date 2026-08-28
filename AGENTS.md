# Research-Agent Repository Instructions

This repository is the source distribution for the Research Agent architecture. It is not an instantiated research project.

## Authority and architecture

- `RESEARCH_AGENT.md` defines the reusable Research Agent behavior.
- `skills/` contains standalone reusable ChatGPT Skills. Each immediate child directory is an independently valid Skill package with its own `SKILL.md` and `agents/openai.yaml`.
- `VERSION` defines the repository-wide semantic version of the Agent/core-Skill distribution.
- `skills-manifest.json` is the machine-readable source manifest for the versioned distribution and complete core Skill set.
- `scripts/package_skills.py` is the deterministic packaging/structural-validation path for release artifacts.
- Project-local instructions used in instantiated research repositories are templates/assets owned by the bootstrap Skill. They must not be confused with this repository's own `AGENTS.md`.
- `README.md`, `Getting-Started.md`, and `USING_IN_YOUR_PROJECT.md` explain installation and use.

Keep the architecture separated into three runtime layers:

1. Agent behavior: reusable research collaboration policy in `RESEARCH_AGENT.md`.
2. Skills: repeatable procedures in `skills/<skill-name>/`.
3. Project state and local rules: files created inside an instantiated research repository, beginning with its own `AGENTS.md`.

Versioned distribution is packaging and compatibility metadata around those layers; it is not a fourth source of project research authority.

Do not reintroduce a central module-routing table or a required `agent/` directory of procedural Markdown modules. A reusable procedure belongs in a Skill. A project-specific convention belongs in the instantiated project's `AGENTS.md` or another project authority. General collaborator behavior belongs in `RESEARCH_AGENT.md`.

## Distribution and releases

- Keep `VERSION` and the `version` / `release_tag` fields in `skills-manifest.json` synchronized.
- Keep the manifest Skill set exactly synchronized with immediate `skills/*/SKILL.md` packages.
- Each Skill must remain independently installable as `skill.zip`; the release bundle may transport multiple independent Skill archives but must never masquerade as one combined Skill.
- Generated `DISTRIBUTION.json`, `dist/`, release manifests, and checksums are build outputs and must not be committed into Skill source directories.
- Bind release artifacts to the exact build commit at packaging time. Do not attempt to hard-code the containing commit SHA into the same source commit.
- Treat `research-agent.lock.json` in an instantiated project as toolchain compatibility metadata only. It never overrides the project's current `AGENTS.md` or research state.
- Do not silently upgrade a project's pin when a newer Research-Agent release exists. A version mismatch requires explicit compatibility review and an intentional lock update.
- See `RELEASES.md` for semantic-versioning and tagged-release procedure.

## Skill maintenance

When adding or changing a Skill:

- keep the Skill trigger description specific enough for reliable auto-selection;
- keep `SKILL.md` focused on the procedure rather than general research philosophy;
- keep project-specific state out of Skills;
- include only resources that materially improve reliability;
- preserve `agents/openai.yaml` UI metadata;
- update `skills-manifest.json` when the core Skill set changes; and
- validate the complete Skill distribution with `python scripts/package_skills.py --output dist` before publishing when execution is available.

Choose and bump the repository-wide version before a tagged release according to `RELEASES.md`. Do not create a tag simply to make CI run; pull requests already validate/package the proposed distribution.

## Repository writes

For substantive changes, create a scoped branch from the current default branch, make only the requested changes, validate them, and open a draft pull request. Do not write directly to the default branch unless explicitly requested. Never force-push or rewrite shared history.
