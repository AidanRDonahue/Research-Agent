# Research-Agent Repository Instructions

This repository is the source distribution for the Research Agent architecture. It is not an instantiated research project.

## Authority and architecture

- `AGENT.md` defines the reusable Research Agent behavior.
- `skills/` contains standalone reusable ChatGPT Skills. Each immediate child directory is an independently valid Skill package with its own `SKILL.md` and `agents/openai.yaml`.
- Project-local instructions used in instantiated research repositories are templates/assets owned by the bootstrap Skill. They must not be confused with this repository's own `AGENTS.md`.
- `README.md` and `Getting-Started.md` explain installation and use.

Keep the architecture separated into three layers:

1. Agent behavior: reusable research collaboration policy in `AGENT.md`.
2. Skills: repeatable procedures in `skills/<skill-name>/`.
3. Project state and local rules: files created inside an instantiated research repository, beginning with its own `AGENTS.md`.

Do not reintroduce a central module-routing table or a required `agent/` directory of procedural Markdown modules. A reusable procedure belongs in a Skill. A project-specific convention belongs in the instantiated project's `AGENTS.md` or another project authority. General collaborator behavior belongs in `AGENT.md`.

## Skill maintenance

When adding or changing a Skill:

- keep the Skill trigger description specific enough for reliable auto-selection;
- keep `SKILL.md` focused on the procedure rather than general research philosophy;
- keep project-specific state out of Skills;
- include only resources that materially improve reliability;
- preserve `agents/openai.yaml` UI metadata; and
- validate the complete Skill package before publishing changes.

## Repository writes

For substantive changes, create a scoped branch from the current default branch, make only the requested changes, validate them, and open a draft pull request. Do not write directly to the default branch unless explicitly requested. Never force-push or rewrite shared history.
