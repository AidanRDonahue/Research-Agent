---
name: bootstrap-research-project
description: Initialize or instantiate a repository as a Research-Agent project. Use when the user asks to bootstrap, initialize, set up, or create a structured research project in a repository, including creating the root task, roadmap, dictionary, templates, project-local AGENTS.md, history, checks, task-folder structure, and a concrete Research-Agent compatibility lock when packaged distribution metadata is available, while preserving existing project artifacts.
---

# Bootstrap Research Project

Initialize the target repository as a persistent, user-directed research workspace.

## Typical project structure

Use the following as the default structure for a bootstrapped project, subject to compatible pre-existing project artifacts and any project-local constraints:

```text
<Project>/
|-- README.md
|-- AGENTS.md
|-- dictionary.md
|-- roadmap.yaml
|-- ROADMAP.md
|-- research-agent.lock.json    # when concrete distribution metadata is available
|-- Tasks/
|   |-- README.md
|   `-- T001-<root-slug>/
|       |-- task-graph.md
|       `-- resolution.md
|-- Background/
|-- templates/
|   |-- task-graph.md
|   `-- resolution.md
|-- history/
|   `-- roadmap-events.jsonl
|-- checks/
|   `-- project-system-checklist.md
`-- <project-specific artifacts>
```

Treat this structure as the visible project outline during bootstrap, not merely as an implementation detail hidden in a reference file. Use `references/project-template.md` for the detailed rules governing each element.

## Workflow

1. Identify the exact target repository and verify its current default branch and write permission.
2. Inspect the current repository before proposing changes. If a project-local `AGENTS.md` already exists, read it first and preserve compatible repository-specific constraints.
3. Gather only the project information needed to initialize faithfully: repository identity, root research question or objective, supplied background, known terminology/conventions, and any explicit repository-specific validation. Leave genuinely unknown details undecided rather than inventing them.
4. For a substantive mutation, create a scoped branch unless the user explicitly asked to write to the default branch.
5. Instantiate the typical project structure shown above using the detailed conventions in `references/project-template.md`. Replace placeholders with the user's supplied project information and preserve existing project-specific files that do not conflict with the project system.
6. If this installed Skill package contains generated `DISTRIBUTION.json` with a concrete Research-Agent version, release tag, source repository, source commit, and `core_skills` list, create `research-agent.lock.json` using those exact values. If concrete distribution metadata is unavailable, do not invent a lock value; report that the project remains unpinned rather than fabricating a version, commit, or Skill set.
7. Create `T001` as the root research task for the overarching question. The root task may remain unresolved while child tasks are defined.
8. Place genuinely shared supplied sources in `Background/`. Do not turn source claims into established project results merely by importing them.
9. Populate `dictionary.md` only with terminology or conventions supported by the user or supplied project authorities.
10. Keep `roadmap.yaml` as canonical structured project state and `ROADMAP.md` as its Mermaid projection with task nodes linking to canonical task folders.
11. Validate the resulting project against the current project-local `AGENTS.md` and project checklist before publishing.
12. Publish the scoped branch through a draft pull request when repository access supports it, unless the user requested another review workflow.

## Boundaries

- Do not copy this source repository's own `AGENTS.md` into the target project. Create a project-local `AGENTS.md` using the baseline in `references/project-template.md`.
- Do not copy `RESEARCH_AGENT.md` or the Skill source directories into every project unless the user explicitly wants a vendored distribution. The Agent and Skills are reusable tooling; the target repository stores project-local state and rules.
- `research-agent.lock.json` records external toolchain compatibility only. It does not override the target project's `AGENTS.md`, roadmap, evidence, or task state.
- Do not prewrite a solution roadmap. Create only the root task and any tasks the user has explicitly authorized.
- Do not invent completed research, evidence, citations, historical state, release versions, commit pins, or installed Skill sets.
