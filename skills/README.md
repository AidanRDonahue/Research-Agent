# Research-Agent Skills

Each immediate child directory is a standalone ChatGPT Skill and should be installed, validated, or packaged independently.

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

Do not combine all Skill directories into one Skill archive. Each package has its own `SKILL.md` entrypoint and UI metadata.
