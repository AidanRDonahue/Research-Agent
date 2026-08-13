# Research Organization Agent

This repository contains a reusable instruction system for creating and maintaining structured research projects. Copy `AGENTS.md` and the `agent/` directory into the root of a target repository, then use those instructions to initialize and operate the project.

`AGENTS.md` is the core authority. It defines repository authority, project conventions, roadmap governance, and the routing table that determines which supporting module is read for a given action. Supporting modules cover bootstrap, repository operations, validation, node workflow, context scoping, and mathematical research.

## What this agent manages

An instantiated project uses the canonical structure defined in `agent/bootstrap.md`:

- `README.md` for project orientation
- `AGENTS.md` and `agent/` for operating instructions
- `dictionary.md` for canonical terminology and notation
- `roadmap.yaml` for canonical project state
- `ROADMAP.md` for the human-readable Mermaid roadmap
- `Tasks/` for one canonical folder per research node
- `Background/` for shared foundations used by multiple tasks
- `templates/` for task templates
- `history/roadmap-events.jsonl` for append-only project-state history
- `checks/project-system-checklist.md` for project-system validation

Task-specific evidence belongs in the corresponding `Tasks/<STABLE-ID>-<slug>/` folder unless it genuinely functions as shared project background.

## Information to provide before initialization

Prepare as much of the following as is known. Leave unknown items explicitly undecided rather than guessing.

### Project identity

Provide:

- repository owner or organization
- repository name
- project title
- concise purpose statement
- project scope and exclusions

These replace generic placeholders such as `<OWNER>/<REPOSITORY>`.

### Project orientation

Describe the research problem or program, intended outputs, expected artifact types, and the working procedure you want contributors to follow.

### Terminology and conventions

Provide domain-specific terminology, definitions, notation, naming rules, units, sign conventions, indexing conventions, normalization rules, and any other conventions that must remain stable. These should become the basis of `dictionary.md`.

### Initial research state

If known, provide the root objective, major existing questions, dependencies, cross-links, completed work, and artifacts that should count as evidence. Roadmap metadata alone should not be treated as evidence.

### Background material

Identify specifications, publications, prior work, accepted assumptions, reference material, design documents, or other sources that should serve as shared foundations across multiple tasks.

### Repository-specific constraints

Provide any required CI commands, tests, linting or formatting commands, branch-protection rules, generated files, preserved directories, validators, or structural requirements.

## Instantiate a new project

First copy these files to the root of the target repository:

```text
AGENTS.md
agent/
├── bootstrap.md
├── repository-operations.md
├── validation.md
├── node-workflow.md
├── context-scoping.md
└── mathematical-research.md
```

Then use a prompt like this:

```text
Initialize this repository as a research project using AGENTS.md.

Repository: <OWNER>/<REPOSITORY>
Project title: <PROJECT TITLE>
Purpose: <PURPOSE>
Scope: <IN-SCOPE WORK>
Out of scope: <EXCLUSIONS>
Primary artifact types: <CODE / PAPERS / DATA / MODELS / EXPERIMENTS / DESIGNS / OTHER>

Project terminology and conventions:
<TERMS, DEFINITIONS, NOTATION, NAMING RULES, UNITS, OR "NONE YET">

Initial research state:
<ROOT OBJECTIVE, KNOWN TASKS, DEPENDENCIES, EXISTING RESULTS, OR "START WITH ONLY A ROOT OBJECTIVE">

Repository-specific validation:
<TESTS, CI, LINTING, STRUCTURAL CHECKS, OR "NO ADDITIONAL VALIDATION YET">

Preserve existing project-specific artifacts that do not conflict with the canonical project system. Do not invent missing research results. Create the required project structure, validate it, and report unresolved decisions or missing inputs.
```

For an empty repository, the minimum useful inputs are repository identity, project title, purpose, scope, and a root objective.

## Upload shared background information

Use this prompt when material should support multiple research tasks:

```text
Add the supplied files and sources as background material for this project.

Inspect each source and preserve its provenance. Put genuinely reusable project-wide material under Background/. Do not treat unsupported claims as established project results. Update dictionary.md only for terminology or conventions supported by the material or explicitly supplied by me. Do not create roadmap tasks merely because a source contains open questions.

After organizing the material, report what was added, where it was placed, what became accepted project-wide context, and what remains source material only.
```

## Upload evidence for one task

Use this prompt when material belongs to a specific node:

```text
Add the supplied material as evidence for task <STABLE-ID>.

Keep it in the canonical Tasks/<STABLE-ID>-<slug>/ folder using an appropriate evidence subdirectory such as notes/, data/, experiments/, scripts/, or references/. Treat it as task-specific unless there is a clear reason it is a shared foundation.

Update the task result-dependency graph only for actual evidence or established results. Do not mark the task completed unless the completion requirements are satisfied.
```

## Define a new research task

```text
Define a new research task for this project. The broad goal is:
<DESCRIBE THE RESEARCH QUESTION OR ACTION>

Use the current roadmap, dictionary, dependencies, and existing evidence as authority. Follow the task-intake workflow in AGENTS.md and the routed node instructions. Do not publish the task until the required intake information is complete.
```

The workflow will establish the action-oriented title, parent, relation to parent, uncertainty reduced, dependencies, bounded method, stopping rules, outcome branches, scope exclusions, assumptions, conventions, validation, and planned result-dependency graph.

## Import existing research work

```text
Reconcile the supplied existing research work with this repository's project system.

For each item, determine whether it belongs in Background/, an existing task folder, a new task folder, or as a project-specific artifact outside the governance directories. Preserve evidence boundaries and do not infer completion from filenames or summaries alone.

Identify any historical state that cannot be reconstructed reliably from the available evidence.
```

## Change project structure

Canonical governance locations must not be replaced by parallel conventions. Project-specific extensions are allowed when they do not displace the responsibilities of `AGENTS.md`, `agent/`, `dictionary.md`, `roadmap.yaml`, `ROADMAP.md`, `Tasks/`, `Background/`, `templates/`, `history/`, or `checks/`.

Use:

```text
Modify the project structure to support this need:
<DESCRIBE THE NEW DIRECTORY, ARTIFACT TYPE, OR WORKFLOW>

Reason:
<WHY THE CURRENT STRUCTURE IS INSUFFICIENT>

Constraints:
<FILES OR DIRECTORIES THAT MUST REMAIN UNCHANGED, MIGRATION REQUIREMENTS, OR OTHER LIMITS>

Preserve the canonical project-system responsibilities. If the requested structure would create a competing canonical location or violate an invariant, explain the conflict and make the smallest compatible alternative change. Validate the resulting structure before publishing it.
```

## Change roadmap structure

```text
Change the roadmap structure as follows:
<DESCRIBE THE MOVE, PARENT CHANGE, DEPENDENCY CHANGE, CROSS-LINK, OR REORGANIZATION>

Do not create a new research node unless required. Preserve stable IDs, verify parent and dependency acyclicity, update display indices when applicable, synchronize roadmap.yaml and ROADMAP.md, preserve direct Mermaid-node links to task folders, and validate the result.
```

## Work on an existing task

```text
Work on research task <STABLE-ID>.

Objective for this session:
<WHAT TO ESTABLISH, TEST, DERIVE, IMPLEMENT, OR ANALYZE>

Use only the task's permitted semantic context under AGENTS.md. Distinguish established facts, cited results, derivations, experiments, numerical evidence, heuristics, and conjectures. Add new task-specific evidence to the canonical task folder and keep its evidence graph synchronized.
```

## Complete a task

```text
Evaluate task <STABLE-ID> for completion and complete it if the repository evidence supports doing so.

Do not rewrite the original question to fit the result. Verify the declared premises and dependencies, produce the required self-contained resolution at the supported scope, update the evidence graph, record outcome separately from lifecycle status, synchronize roadmap.yaml and ROADMAP.md, append required history, and validate the project.
```

Negative and inconclusive outcomes should be recorded accurately rather than converted into artificial success outcomes.

## Validate a project

```text
Validate this repository against AGENTS.md and the routed validation instructions.

Check the canonical structure, roadmap/task consistency, stable IDs, parent and dependency validity, task folders, required task files, pending versus completed resolutions, evidence graphs, templates, history, terminology conventions, and checks/project-system-checklist.md. Also run any repository-specific validators that are available.

Report failures and validation limitations explicitly.
```

## Recommended first-use sequence

1. Copy `AGENTS.md` and `agent/` into the target repository.
2. Supply project identity, purpose, scope, terminology, initial state, and repository-specific constraints.
3. Run the initialization prompt.
4. Review the generated project `README.md`, `dictionary.md`, roadmap, templates, and validation checklist.
5. Add shared sources to `Background/` with the background-information prompt.
6. Define the first bounded task using the task-intake workflow.
7. Work by stable task ID and keep task evidence inside its canonical folder.
8. Complete tasks only when their evidence and validation requirements are satisfied.
9. Use structural-change prompts instead of creating parallel project conventions manually.
10. Validate before merging structural or task-completion changes.
