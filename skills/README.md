# Research-Agent Skills

Each immediate child directory is a standalone ChatGPT Skill and must remain independently installable, validatable, and packageable.

The Skills are intentionally procedural. They rely on the Research Agent for general collaboration behavior and on the target repository's `AGENTS.md` for local project rules.

Current packages:

- `bootstrap-research-project`
- `define-research-task`
- `transcribe-research-evidence`
- `review-mathematical-result`
- `restructure-research-roadmap`
- `complete-research-task`
- `validate-research-project`
- `synthesize-research-project`

`skills-manifest.json` at the repository root is the machine-readable list of the core packages in a versioned distribution. `scripts/package_skills.py` validates that the source tree and manifest agree and emits one `<skill-name>/skill.zip` for each Skill.

The release-level `research-agent-skills-v<VERSION>.zip` is a convenience bundle containing those independent archives. It is **not** itself a Skill. Extract the bundle and install the individual `skill.zip` files.

Generated package metadata is injected as `DISTRIBUTION.json` during packaging so an installed Skill can identify the exact Research-Agent version and source commit. Do not commit that generated file into a Skill source directory.
