# General Research Project — Agent Instructions

These instructions govern repository-aware research and roadmap work in `<OWNER>/<REPOSITORY>`.

## Repository authority

- Treat this repository's current default branch and current files as the primary source of truth.
- Do not invent repository contents, task state, research results, sources, validation results, or outcomes.
- Preserve evidence boundaries: roadmap metadata is not independent proof.
- When files disagree, prefer current authorities in this order: `AGENTS.md`, `dictionary.md`, current research artifacts, `roadmap.yaml`, `ROADMAP.md`, append-only history.
- The canonical repository is `<OWNER>/<REPOSITORY>`.

## Context discipline

For node-scoped work, semantic context normally contains only the task being worked on, its conceptual parent, declared dependencies, required cross-links, and directly attached task-folder evidence. Do not automatically import unrelated roadmap branches. Repository-wide metadata may be inspected for structural validation only.

## Research rigor

Classify claims when useful as established fact, cited result, derivation, experimental evidence, numerical evidence, heuristic, or conjecture. Scrutinize assumptions, dimensions, domains/codomains, quantifiers, regularity, compatibility conditions, singular cases, sign conventions, indexing, normalization, and other domain-specific hypotheses. Finite enumeration is evidence only unless it exactly exhausts the explicit finite certificate being claimed.

When a statement fails, identify the exact failure and make only the strongest repair justified by evidence. Keep exact conclusions, statistical conclusions, ordering relations, structural equivalence, experimental evidence, and numerical evidence distinct.

## Project terminology and conventions

Use `dictionary.md` as the canonical project vocabulary and notation authority. Preserve project-defined terminology, identifiers, naming conventions, domain-specific definitions, and current symbol meanings exactly.

When mathematical Markdown is used, prefer GitHub's backtick-delimited inline form ``$`...`$``. For display math, prefer fenced `math` blocks when dollar-delimited display math is unreliable. Do not use `\tag{...}` inside fenced `math` blocks. For numbered display equations, put the equation number in ordinary Markdown immediately outside the fenced block and keep references such as `(1)` in prose. Preserve TeX backslashes exactly and follow any additional mathematical conventions recorded in `dictionary.md` or other designated project authorities.

## Roadmap governance

`roadmap.yaml` is the canonical structured roadmap and project-state source. `ROADMAP.md` is its human-readable or visual projection.

Stable IDs use the repository-defined format, such as `A01`, `A02`, and so on. They are allocated monotonically, are never reused, and do not encode hierarchy or topic. `display_index`, when used, is the mutable hierarchical front-facing index. Every non-root work item has exactly one conceptual parent. Dependencies are prerequisite information flow; cross-links are non-parent relationships. Parent and dependency graphs must be acyclic.

Every work item represented in `ROADMAP.md` must link to its canonical folder under `Tasks/`.

## Mandated repository structure

The project must use the following top-level structure. These paths and responsibilities are canonical unless this file explicitly permits a project-specific extension.

```text
<Project>/
│
├── README.md
│   └── Project orientation
│       ├── purpose
│       ├── scope
│       ├── repository structure
│       └── working procedure
│
├── AGENTS.md
│   └── Rules for humans and automated agents
│       ├── operating principles
│       ├── workflow
│       ├── change discipline
│       ├── project conventions
│       └── validation requirements
│
├── dictionary.md
│   └── Canonical project vocabulary
│       ├── terminology
│       ├── identifiers
│       ├── naming conventions
│       └── domain-specific definitions
│
│
├── roadmap.yaml
│   └── CANONICAL PROJECT STATE
│       ├── project metadata
│       ├── ID policy
│       ├── hierarchy policy
│       └── work items
│           ├── parent
│           ├── dependencies
│           ├── status
│           ├── objective
│           ├── method / execution plan
│           ├── deliverables
│           └── outcome branches
│
├── ROADMAP.md
│   └── Human-readable / visual projection of roadmap.yaml
│       └── each item links → its canonical work folder
│
│
├── Tasks/
│   │
│   ├── README.md
│   │   └── Defines the work-item folder convention
│   │
│   ├── A01-<short-title>/
│   │   ├── task-graph.md
│   │   │   └── contract + internal dependency/result graph
│   │   │
│   │   ├── resolution.md
│   │   │   └── canonical completion record / final synthesis
│   │   │
│   │   └── supporting files
│   │       ├── notes/
│   │       ├── data/
│   │       ├── designs/
│   │       ├── experiments/
│   │       ├── scripts/
│   │       ├── references/
│   │       └── other task-specific evidence
│   │
│   ├── A02-<short-title>/
│   │   ├── task-graph.md
│   │   ├── resolution.md
│   │   └── ...
│   │
│   └── ...
│
│
├── Background/
│   └── Shared foundations reused by multiple tasks
│       ├── specifications
│       ├── prior work
│       ├── reference material
│       └── accepted project-wide knowledge
│
├── templates/
│   ├── task-graph.md
│   ├── resolution.md
│   └── node-card.md
│       └── Canonical templates for new work items
│
├── history/
│   └── roadmap-events.jsonl
│       └── Append-only project-state transition history
│
├── checks/
│   └── project-system-checklist.md
│       └── Manual or automated project validation
│
└── <project-specific artifacts>
    └── Source code, product files, publications,
        models, assets, deployments, etc.
```

The listed governance files and directories are part of the project system and must not be replaced by parallel conventions.

Project-specific artifacts may be added at the repository root or in appropriate project-specific directories, but they must not displace or redefine the canonical responsibilities of `README.md`, `AGENTS.md`, `dictionary.md`, `roadmap.yaml`, `ROADMAP.md`, `Tasks/`, `Background/`, `templates/`, `history/`, or `checks/`.

Do not create competing locations for canonical project state, task contracts, task resolutions, shared foundations, templates, or project-state history.

## Canonical task-folder convention

Every roadmap work item has exactly one canonical folder:

```text
Tasks/<STABLE-ID>-<short-title>/
├── task-graph.md
├── resolution.md
└── ... task-specific supporting evidence
```

The folder name begins with the stable ID. `Tasks/README.md` defines the repository-wide work-item folder convention and must remain consistent with this file.

Do not create new single-file task contracts such as `Tasks/A08-title.md`, and do not create a separate task-resolution directory or parallel task-storage convention for new work.

### `task-graph.md`

`task-graph.md` is both the task contract and the task's internal result-dependency graph. It must preserve the original research or project question and include:

- stable ID, display index when applicable, title, type, and status;
- exactly one conceptual parent except for the root;
- relation to parent and effect on parent;
- uncertainty reduced/question answered;
- exact dependencies and required cross-links using stable IDs;
- objective;
- bounded method or execution plan and stopping rules;
- canonical task-local `resolution.md` deliverable;
- success, negative, and realistic inconclusive branches;
- scope exclusions, assumptions, terminology/conventions, and independent validation; and
- a Mermaid result graph.

The Mermaid result graph is an **evidence graph for the task folder**, not a workflow or process diagram. It must show how the task question is answered by task-local evidence files/results and how those evidence artifacts depend on one another to support the resulting conclusion.

When a supporting evidence file is added to the task folder, include a graph node labeled with that filename, or with that filename together with the established result it contains, and connect it from the evidence/result it uses to the consequence it establishes.

Prefer the smallest graph that matches the actual evidentiary chain. When the evidence is sequential, use a linear chain such as `Question --> first evidence/result --> second evidence/result`. Do not add generic process nodes such as “derive,” “validate,” “test,” or “synthesize” unless they correspond to an inspectable artifact or an established result that is itself evidence for a later node.

An edge points **from evidence/result to a consequence that uses it**. When two or more evidence files/results are jointly required for a later result, that later node has one incoming edge from each required input. Every material task-local evidence file/result needed for the resolution should lie on a path from the task question to the final established result.

The graph should make it possible to see which evidence files build on which earlier evidence without reconstructing that dependency from prose alone.

Do not confuse this task-internal evidence graph with the repository-wide roadmap task tree.

### `resolution.md`

`resolution.md` is always present.

Before completion it contains an explicit pending notice and must not assert a resolved outcome. When the task completes, it becomes the canonical self-contained completion record and final synthesis explaining exactly how the task was resolved.

For a theorem, lemma, proposition, identity, construction theorem, impossibility result, or other formal claim, the completed resolution must contain the full proof at the exact proved scope.

For a negative result, include the exact counterexample, failure certificate, experimental result, or other evidence required to show that the original claim or objective failed.

For an inconclusive result, explain the exact obstruction reached and what was established before the obstruction.

A resolution may assume only the established results of its declared parent and dependencies. It must state assumptions, edge cases, claim boundaries, and validation. It should not require the reader to reconstruct the central argument by following unrelated files.

### Supporting evidence

Task-specific notes, data, designs, experiments, scripts, references, papers, source excerpts, computations, exact certificates, conversation/research notes, or other artifacts needed to write or audit the resolution belong inside the same task folder.

Use descriptive subfolders such as:

- `notes/`
- `data/`
- `designs/`
- `experiments/`
- `scripts/`
- `references/`

Additional task-specific evidence directories may be created when useful.

Shared foundations that genuinely support multiple tasks belong in `Background/`; otherwise prefer task-local evidence.

## Shared foundations

`Background/` contains accepted or reusable foundations that support multiple work items.

Appropriate contents include:

- specifications;
- prior work;
- reference material; and
- accepted project-wide knowledge.

Do not move task-specific evidence into `Background/` merely because it may be useful later. Material belongs in `Background/` only when it genuinely functions as a shared project foundation.

## Canonical templates

`templates/` contains the canonical templates used when creating new work items.

At minimum it contains:

```text
templates/
├── task-graph.md
├── resolution.md
└── node-card.md
```

Use these templates when creating new tasks. Do not silently substitute locally invented formats when the canonical template exists.

## Project-state history

`history/roadmap-events.jsonl` is the append-only project-state transition history.

Do not rewrite or reorder existing history entries. Append new events only when repository rules require a recorded state transition.

History records are supporting state history; they do not override the current canonical state in `roadmap.yaml`.

## Project validation

`checks/project-system-checklist.md` defines the manual or automated project-system validation procedure.

Repository validators, scripts, or CI checks may extend this validation, but they must remain consistent with the invariants defined in this file.

## Defining a new task

When asked to define, create, or add a task, do not write during intake. Begin exactly with:

> What concrete action and bounded target should this task have?

Gather one precise item at a time until the task has an action-oriented title, type, status, one parent, relation to parent, uncertainty reduced, effect on parent, dependencies, bounded method, stopping rules, outcome branches, scope exclusions, assumptions, terminology/conventions, independent validation, and a planned result-dependency graph.

At publication time:

1. assign the next unused stable ID and correct `display_index` when applicable;
2. create `Tasks/<STABLE-ID>-<slug>/`;
3. copy `templates/task-graph.md` to the new folder as `task-graph.md`;
4. copy `templates/resolution.md` to the new folder as `resolution.md`;
5. populate the task graph completely, including its Mermaid result DAG;
6. keep the resolution explicitly pending;
7. place any supplied task-specific sources, notes, data, designs, experiments, scripts, references, or other evidence in the same task folder;
8. synchronize `roadmap.yaml` and `ROADMAP.md`; and
9. append `history/roadmap-events.jsonl` when required.

Do not renumber existing stable IDs when inserting or moving a task.

## Completing a task

Before marking a work item completed:

1. verify that all required premises/results in `task-graph.md` are established or explicitly accounted for;
2. verify that `resolution.md` answers the original task without rewriting the question to fit the result;
3. write the complete proof, derivation, construction, design, counterexample, experiment synthesis, exact calculation, implementation result, or other required resolution in `resolution.md`;
4. update the result graph so the established evidence path to the conclusion is explicit;
5. set lifecycle status separately from scientific, technical, or project outcome;
6. preserve negative and inconclusive results as substantive work;
7. record completion date, outcome, concise result summary, supporting artifact paths, successors, validation, and warnings in `task-graph.md`;
8. synchronize `roadmap.yaml` and `ROADMAP.md`; and
9. append history when repository rules require a roadmap transition.

## Repository write discipline

For substantive changes: verify repository identity, default branch, and push permission; reread target files and blob SHAs; create a scoped branch; make only requested changes; validate; push; and open a draft pull request.

Do not write directly to the default branch unless explicitly asked. Never force-push or rewrite shared history.

## Validation gate

Before publishing project-system, task, or roadmap changes, verify:

- all mandated top-level files and directories exist;
- `README.md` documents project purpose, scope, repository structure, and working procedure;
- `AGENTS.md` defines operating principles, workflow, change discipline, project conventions, and validation requirements;
- `dictionary.md` defines canonical terminology, identifiers, naming conventions, and domain-specific definitions;
- `roadmap.yaml` remains the canonical project-state source;
- `ROADMAP.md` is a valid human-readable or visual projection of `roadmap.yaml`;
- every roadmap item links to its canonical work folder;
- stable IDs are unique, valid, and not reused;
- display indices, when used, are unique and consistent with the conceptual tree;
- each non-root node has exactly one existing parent;
- parent/dependency graphs are acyclic;
- dependency and cross-link targets exist and use stable IDs;
- every roadmap work item has exactly one `Tasks/<ID>-<slug>/` folder;
- `Tasks/README.md` exists and agrees with the canonical task-folder convention;
- every task folder contains both `task-graph.md` and `resolution.md`;
- every task graph has required metadata, objective, execution plan, stopping rules, outcome branches, scope, assumptions, conventions, validation, and a Mermaid result graph;
- task-graph nodes and edges reflect the actual task-local evidence files/results and their dependency order rather than generic workflow steps;
- every task-local evidence file/result required by the resolution is represented on a path from the task question to the established result;
- unresolved resolutions are explicitly pending and do not assert outcomes;
- completed nodes have completion metadata and a self-contained resolution;
- completed formal results contain complete proofs or equivalent exact evidence where required;
- supporting evidence referenced by a resolution exists in the same task folder or is an explicitly shared foundation in `Background/`;
- the canonical files in `templates/` exist and are used for new work items;
- `roadmap.yaml` agrees with task folders and completion artifacts;
- history remains valid append-only JSONL in `history/roadmap-events.jsonl`;
- `checks/project-system-checklist.md` exists and remains consistent with current project-system requirements;
- repository terminology and conventions are preserved; and
- project-specific artifacts do not replace, duplicate, or contradict the canonical project-system structure.

If an available validator assumes a retired repository or task layout, do not report it as passing the current layout. Perform the strongest available manual or migration-specific structural validation and state that limitation explicitly.

After a successful mutation, report project state, files changed, branch, commit(s), draft pull request, validation performed, and unresolved warnings.