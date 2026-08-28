# Research Agent

Research Agent is a framework for guided work on long, branching research questions. It is designed to keep a model anchored to the user's actual research program across many conversations without asking the model to autonomously finish the entire problem.

The architecture separates three concerns that were previously mixed together:

1. **Agent behavior** - how the research collaborator should behave.
2. **Skills** - repeatable procedures such as defining a task or transcribing evidence.
3. **Project repository** - local rules, state, notation, roadmap, tasks, evidence, and history for one research project.

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for the design in more detail.

## Why this separation matters

Long research projects tend to fail when general model behavior, procedural instructions, and project state all live in one large prompt. The model may load irrelevant instructions, lose track of what is local versus reusable, or treat a task plan as permission to run ahead.

This repository instead uses:

- [`RESEARCH_AGENT.md`](RESEARCH_AGENT.md) for the reusable collaborator mandate;
- [`skills/`](skills/) for standardized operations; and
- a project-local `AGENTS.md` inside each instantiated research repository for that project's own rules and authorities.

The guiding rule is:

> **Agent = behavior. Skill = procedure. Project repository = state and local rules.**

## Core research behavior

The Research Agent is intended for user-directed research rather than autonomous completion.

A normal task conversation looks like:

```text
User chooses the next bounded question or research step
        |
        v
Agent works deeply on that step
        |
        v
Result or evidence is inspected and optionally preserved
        |
        v
Agent states what is established and what remains open
        |
        v
User chooses the next direction
```

Creating a task does not authorize the model to execute every step in the task plan. Completing a task is a separate explicit workflow.

## Repository contents

```text
Research-Agent/
|-- AGENTS.md
|   `-- instructions for maintaining this source repository
|
|-- RESEARCH_AGENT.md
|   `-- reusable Research Agent behavior
|
|-- ARCHITECTURE.md
|   `-- agent / skill / project separation
|
|-- skills/
|   |-- bootstrap-research-project/
|   |-- define-research-task/
|   |-- transcribe-research-evidence/
|   |-- complete-research-task/
|   `-- validate-research-project/
|
|-- Getting-Started.md
`-- README.md
```

The old `agent/*.md` manual module system is intentionally retired. Its reusable procedures have been moved into standalone Skills, and its project-local rules have been moved into the project template owned by the bootstrap Skill.

## The Agent

[`RESEARCH_AGENT.md`](RESEARCH_AGENT.md) contains the small persistent mandate that should stay active throughout research. It covers:

- user-directed bounded work;
- evidence and claim discipline;
- repository grounding;
- task-completion boundaries;
- meaningful decision points;
- research rigor; and
- safe repository mutation defaults.

It intentionally does **not** define the exact task-folder schema, roadmap IDs, or the state of any particular research project.

## The Skills

Each immediate child of [`skills/`](skills/) is a standalone ChatGPT Skill.

### `bootstrap-research-project`

Use when creating or initializing a structured research repository. It owns the reusable project templates and creates the root task, roadmap, dictionary, task conventions, history, and validation structure.

### `define-research-task`

Use when the user wants to define, create, add, or branch a new research task. It conducts guided intake, then publishes the new task without solving it.

### `transcribe-research-evidence`

Use when the user wants specified content faithfully preserved as Markdown evidence in an existing task folder. It does not interpret the evidence or advance task state.

### `complete-research-task`

Use only when the user explicitly asks to evaluate, resolve, synthesize, or complete a task. It verifies the evidence and writes the canonical resolution at the supported scope.

### `validate-research-project`

Use when auditing project structure, roadmap/task consistency, evidence boundaries, history, terminology, or changed mathematics.

Each Skill must be installed or packaged independently. Do not combine the entire `skills/` directory into one Skill archive.

## Project-local `AGENTS.md`

An instantiated research repository gets its own `AGENTS.md`. The bootstrap Skill's project template defines the default local contract.

That file answers questions such as:

- Which files are authoritative for this project?
- What is the canonical roadmap state?
- How are stable task IDs allocated?
- What context may be loaded for one task?
- What task-folder structure is required?
- What notation and terminology rules apply?
- What repository validation must run?

A project-local `AGENTS.md` should not manually route the model to procedural Markdown modules. Skills provide procedure selection; the project file provides local authority.

## Typical project structure

A bootstrapped project normally looks like:

```text
<Project>/
|-- README.md
|-- AGENTS.md
|-- dictionary.md
|-- roadmap.yaml
|-- ROADMAP.md
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

The project repository stores persistent research state. The Agent and Skills are reusable tooling and do not need to be vendored into every project unless the user deliberately wants a self-contained copy.

## Quick start

1. Connect ChatGPT to GitHub and configure the connector's repository access.
2. Use [`RESEARCH_AGENT.md`](RESEARCH_AGENT.md) as the persistent instructions for the Research Agent or GPT that will conduct the research.
3. Install the standalone Skills in [`skills/`](skills/) that you want available.
4. Ask the Agent to bootstrap a target repository around a root research question.
5. Work through tasks conversationally, preserving important intermediate results as evidence.
6. Explicitly request task completion only when you want the resolution workflow to run.

A minimal bootstrap request is:

```text
Initialize <OWNER>/<REPOSITORY> as a Research-Agent project around the question:
"<ROOT RESEARCH QUESTION>"

Use <SUPPLIED MATERIAL> as background.
```

A typical new-task request is:

```text
I want to create a new task branching from T001. Start the task-definition conversation.
```

A typical evidence request is:

```text
Transcribe the result we just established as evidence for T004 and save it as notes/<FILENAME>.md.
```

A typical completion request is:

```text
Evaluate T004 for completion and complete it if the evidence supports an outcome.
```

See [`Getting-Started.md`](Getting-Started.md) for a full first-project walkthrough.

## Design principle

The roadmap should remain a map of the research, not a solution written in advance. Broad questions can branch as useful directions emerge. Completed branches can later support a synthesis, while unused branches remain explicit starting points for follow-up work.
