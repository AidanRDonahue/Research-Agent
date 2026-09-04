# Research Agent

Research Agent is a framework for guided work on long, branching research questions. It keeps a model anchored to the user's actual research program across many conversations without treating a task plan as permission to autonomously finish the entire problem.

The architecture separates three runtime concerns:

1. **Agent behavior** — how the research collaborator should behave.
2. **Skills** — repeatable procedures such as defining a task, digesting a paper, or transcribing evidence.
3. **Project repository** — local rules, state, notation, roadmap, tasks, evidence, and history for one research project.

A versioned distribution layer makes the reusable Agent/Skill toolchain reproducible without mixing it into project state.

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for the design and [`USING_IN_YOUR_PROJECT.md`](USING_IN_YOUR_PROJECT.md) for the complete consumer tutorial.

## Guiding rule

> **Agent = behavior. Skill = procedure. Project repository = state and local rules. Distribution = versioned packaging and compatibility metadata.**

Long research projects tend to fail when general model behavior, procedural instructions, and project state all live in one large prompt. This repository instead uses:

- [`RESEARCH_AGENT.md`](RESEARCH_AGENT.md) for the reusable collaborator mandate;
- [`skills/`](skills/) for standardized operations;
- a project-local `AGENTS.md` inside each instantiated research repository for that project's own rules and authorities; and
- [`VERSION`](VERSION), [`skills-manifest.json`](skills-manifest.json), and release tooling for a reproducible external toolchain.

## Versioned distribution

`VERSION` is the semantic version of the Agent/core-Skill suite. `skills-manifest.json` lists the complete Skill set associated with that source version.

Running:

```bash
python scripts/package_skills.py --output dist
```

validates the manifest/source layout and creates deterministic artifacts:

```text
dist/
|-- research-agent-distribution.json
|-- research-agent-skills-v<VERSION>.zip
|-- SHA256SUMS
|-- bootstrap-research-project/
|   `-- skill.zip
|-- complete-research-task/
|   `-- skill.zip
`-- ... one skill.zip per core Skill
```

Every `skill.zip` remains an independent ChatGPT Skill. The outer `research-agent-skills-v<VERSION>.zip` is only a convenience transport bundle; extract it before installing Skills.

The generated `research-agent-distribution.json` binds the distribution to the exact source commit. Each Skill archive also receives generated `DISTRIBUTION.json` metadata with the same release identity.

Tagged `v<VERSION>` builds are published by [`.github/workflows/release-skills.yml`](.github/workflows/release-skills.yml). Pull requests run the same validation/packaging job and expose the proposed packages as a workflow artifact.

See [`RELEASES.md`](RELEASES.md) for the release procedure.

## Project compatibility pins

A project may store `research-agent.lock.json` to record which external Research-Agent release it was tested against. The lock records the source repository, version, release tag, source commit, and required Skills.

The lock is not research authority. It never overrides the project's `AGENTS.md`, dictionary, roadmap, task evidence, or current repository state.

A newer Research-Agent release should not silently update the lock. Compare intentionally, test the new toolchain, reconcile project-local differences, and then update the pin.

Use [`templates/research-agent.lock.example.json`](templates/research-agent.lock.example.json) when a bootstrap environment cannot read generated package metadata.

## Core research behavior

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
|-- RESEARCH_AGENT.md
|-- ARCHITECTURE.md
|-- VERSION
|-- skills-manifest.json
|-- RELEASES.md
|-- USING_IN_YOUR_PROJECT.md
|-- scripts/
|-- templates/
|-- skills/
|   |-- bootstrap-research-project/
|   |-- define-research-task/
|   |-- paper-digest/
|   |-- transcribe-research-evidence/
|   |-- review-mathematical-result/
|   |-- restructure-research-roadmap/
|   |-- complete-research-task/
|   |-- validate-research-project/
|   `-- synthesize-research-project/
|-- Getting-Started.md
`-- .github/workflows/release-skills.yml
```

The old `agent/*.md` manual module system is intentionally retired. Reusable procedures are standalone Skills; project-local rules belong in the project template owned by the bootstrap Skill.

## The Agent

[`RESEARCH_AGENT.md`](RESEARCH_AGENT.md) contains the small persistent mandate that should stay active throughout research. It covers user-directed bounded work, evidence and claim discipline, repository grounding, task-completion boundaries, meaningful decision points, rigor, safe repository mutation defaults, and awareness of an explicit project toolchain pin.

It intentionally does **not** define the exact task-folder schema, roadmap IDs, or the state of any particular research project.

## The Skills

Each immediate child of [`skills/`](skills/) is a standalone ChatGPT Skill:

- **`bootstrap-research-project`** initializes a structured research repository and records a concrete Research-Agent compatibility lock when packaged distribution metadata is available.
- **`define-research-task`** conducts guided intake and publishes a new bounded task without solving it.
- **`paper-digest`** turns one paper into a nested Markdown background package with source coverage, inquiry-tree navigation, typed claims/evidence, theorem/proof structure, and relations while keeping paper-derived material distinct from established project results.
- **`transcribe-research-evidence`** preserves specified content faithfully as task-local Markdown evidence.
- **`review-mathematical-result`** adversarially audits a theorem, proof, derivation, bound, or argument without automatically changing project state.
- **`restructure-research-roadmap`** reorganizes task relationships while preserving identity, evidence, negative/inconclusive branches, and history.
- **`complete-research-task`** runs only when completion is explicitly requested and writes the supported canonical resolution.
- **`validate-research-project`** audits structure, roadmap/task consistency, evidence boundaries, history, terminology, and applicable mathematics.
- **`synthesize-research-project`** builds higher-level exposition from established project results while preserving exact hypotheses and unresolved gaps.

Do not combine the entire `skills/` source directory into a single Skill archive.

## Project-local `AGENTS.md`

An instantiated research repository gets its own `AGENTS.md`. The bootstrap Skill's project template defines the default local contract. That file answers which files are authoritative, how roadmap/task state works, what context may be loaded, what notation rules apply, and what validation must run.

A project-local `AGENTS.md` should not manually route the model to procedural Markdown modules. Skills provide procedure selection; the project file provides local authority.

## Quick start

For a stable installation:

1. Choose a tagged Research-Agent release.
2. Use `RESEARCH_AGENT.md` from that tag as the persistent instructions for your research GPT/agent.
3. Download and extract `research-agent-skills-v<VERSION>.zip`.
4. Install the individual `skill.zip` packages you want available.
5. Connect ChatGPT to the target GitHub repository.
6. Ask the Agent to bootstrap the target around a root research question.
7. Preserve the resulting `research-agent.lock.json` when concrete release metadata is available.
8. Work through tasks conversationally and request completion only when you intend the completion workflow to run.

A minimal bootstrap request is:

```text
Initialize <OWNER>/<REPOSITORY> as a Research-Agent project around the question:
"<ROOT RESEARCH QUESTION>"

Use <SUPPLIED MATERIAL> as background.
```

See [`USING_IN_YOUR_PROJECT.md`](USING_IN_YOUR_PROJECT.md) for installation, pinning, daily workflow, upgrading, development packaging, and troubleshooting.

## Design principle

The roadmap should remain a map of the research, not a solution written in advance. Broad questions can branch as useful directions emerge. Completed branches can later support a synthesis, while unused branches remain explicit starting points for follow-up work.
