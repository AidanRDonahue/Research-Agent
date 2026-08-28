# Research-Agent Installation Guide

A concise setup guide for using Research-Agent with a GitHub repository that organizes long-running research.

## 1. The mental model

Research-Agent has three runtime layers:

```text
ChatGPT / research GPT
  RESEARCH_AGENT.md = collaborator behavior
  installed Skills  = repeatable procedures
            |
            v
GitHub research repository
  AGENTS.md + dictionary + roadmap + tasks + evidence
```

The Agent and Skills are normally **not copied into the research repository**. They are installed/configured in ChatGPT. The GitHub repository stores project-local rules, durable research state, and an optional `research-agent.lock.json` compatibility pin.

## 2. Prepare ChatGPT and GitHub

1. Create or choose the GitHub repository that will hold the research.
2. Connect ChatGPT to GitHub and grant access to that repository.
3. Use `RESEARCH_AGENT.md` from one Research-Agent version as the persistent instructions for the research GPT/agent.
4. Install the Research-Agent Skills from the same version in ChatGPT.

For a complete workflow install:

- `bootstrap-research-project`
- `define-research-task`
- `transcribe-research-evidence`
- `review-mathematical-result`
- `restructure-research-roadmap`
- `complete-research-task`
- `validate-research-project`
- `synthesize-research-project`

Each Skill is installed independently as its own `skill.zip`. The outer Research-Agent release bundle, when present, is only a transport archive and is not itself a Skill.

## 3. Package from source when no release bundle is available

Clone and pin the Research-Agent source you want to use:

```bash
git clone https://github.com/AidanRDonahue/Research-Agent.git
cd Research-Agent
git checkout <EXACT-COMMIT-OR-TAG>
python scripts/package_skills.py --output dist
```

Then install the individual packages under:

```text
dist/<skill-name>/skill.zip
```

Keep `dist/research-agent-distribution.json`; it records the exact version and source commit used to build the packages.

## 4. Bootstrap the research repository

After the Agent and Skills are available in ChatGPT, ask:

```text
Initialize OWNER/REPOSITORY as a Research-Agent project around the question:
"<ROOT RESEARCH QUESTION>"

Use the existing material in <PATH> as supplied background.
Do not invent research conclusions or future tasks.
```

The bootstrap workflow inspects the repository first and then creates the project-local research system. A typical repository becomes:

```text
README.md
AGENTS.md
dictionary.md
roadmap.yaml
ROADMAP.md
research-agent.lock.json   # when concrete distribution metadata is available
Tasks/
Background/
templates/
history/
checks/
```

The root task begins pending. Bootstrap organizes the research; it does not solve it or prewrite the future roadmap.

## 5. Everyday research workflow

Ordinary research is conversational. Name the current task and the bounded question:

```text
Work with me on T002. For this turn, determine whether the current assumptions
are sufficient for the proposed bound. Do not continue to later proof steps.
```

Use natural-language requests for standardized procedures:

| Goal | Example request |
| --- | --- |
| Define a task | `Define a new task under T002 for this obstruction.` |
| Review mathematics | `Review the current lemma adversarially.` |
| Save evidence | `Transcribe the verified proof as evidence for T002.` |
| Restructure | `Make this obstruction a sibling task and preserve history.` |
| Complete | `Evaluate T002 for completion and complete it only if supported.` |
| Validate | `Validate this branch against the current project rules.` |
| Synthesize | `Synthesize the completed tasks into a paper-level outline.` |

A Skill supplies the reusable procedure. The project's current `AGENTS.md` supplies the local rules and wins if there is a conflict.

## 6. What belongs where

```text
AidanRDonahue/Research-Agent
  reusable Agent + Skill source + release tooling

ChatGPT
  persistent Research-Agent instructions
  installed Skill packages

Your GitHub research repository
  AGENTS.md
  dictionary.md
  research-agent.lock.json
  roadmap.yaml / ROADMAP.md
  Tasks/ and evidence
  Background/
  history/ and checks/
```

Do not vendor the Skill source into the research repository unless you deliberately want a self-contained source snapshot.

## 7. Upgrade safely

Do not make a research project follow `Research-Agent/main` automatically.

When a newer release is available:

1. read the release changes;
2. install the updated Agent/Skill distribution in ChatGPT;
3. test it against the project on a branch;
4. compare it with the existing `research-agent.lock.json`;
5. reconcile any project-local workflow changes; and
6. update the lock only after intentionally accepting the new release.

If you have a Research-Agent checkout, compatibility can be checked with:

```bash
python scripts/check_project_compatibility.py \
  /path/to/project/research-agent.lock.json \
  --distribution /path/to/research-agent-distribution.json
```

A mismatch is a review signal, not permission for an automatic migration.

## Quick-start checklist

- [ ] GitHub research repository exists.
- [ ] ChatGPT can access it.
- [ ] `RESEARCH_AGENT.md` is configured as persistent agent behavior.
- [ ] Required Skills are installed independently.
- [ ] Project has been bootstrapped.
- [ ] Project-local `AGENTS.md` is treated as the operating authority.
- [ ] Toolchain version is pinned when concrete distribution metadata is available.
- [ ] Research proceeds through bounded, user-directed task conversations.

Source: `AidanRDonahue/Research-Agent`, Research-Agent v0.1.0 architecture.