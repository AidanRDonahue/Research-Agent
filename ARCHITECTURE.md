# Architecture

The Research Agent is intentionally split into three layers.

## 1. Agent

`RESEARCH_AGENT.md` defines how the research collaborator behaves: user-directed work, bounded scope, evidence discipline, repository grounding, decision points, and completion boundaries.

The Agent answers: **How should the collaborator behave?**

## 2. Skills

Each directory under `skills/` is a standalone reusable Skill for a repeatable operation. Skills are loaded when their trigger matches the user's request.

The Skills answer: **How should this particular operation be performed?**

Current Skills:

- `bootstrap-research-project`: initialize an empty or existing repository as a structured research project.
- `define-research-task`: conduct task intake and publish a new bounded research task.
- `transcribe-research-evidence`: faithfully record specified content as task-local Markdown evidence.
- `complete-research-task`: evaluate and synthesize a task into its canonical resolution when completion is explicitly requested.
- `validate-research-project`: audit project structure, roadmap/task consistency, evidence boundaries, and applicable mathematical writes.

## 3. Project repository

An instantiated project contains its own `AGENTS.md`, `dictionary.md`, roadmap, task folders, evidence, templates, history, and project-specific artifacts.

The project repository answers: **What is true here, and what local rules govern this project?**

A project `AGENTS.md` is not the Research Agent itself. It is the local operating contract for that repository. Skills must read it before acting on project state.

## Dependency direction

```text
User request
    |
    v
Research Agent behavior (`RESEARCH_AGENT.md`)
    |
    +---- matching Skill ----------------+
    |                                    |
    v                                    v
bounded research work             standardized procedure
    |                                    |
    +----------------+-------------------+
                     |
                     v
             project repository
             reads local `AGENTS.md`
             and current project state
```

The important rule is that reusable Skills do not own project state and project repositories do not manually route procedural modules.
