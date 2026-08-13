# Node workflow

## Canonical task-folder convention

Every roadmap work item has exactly one canonical folder:

```text
Tasks/<STABLE-ID>-<short-title>/
├── task-graph.md
├── resolution.md
└── ... task-specific supporting evidence
```

The folder name begins with the stable ID. `Tasks/README.md` defines the repository-wide work-item folder convention and must remain consistent with this file.

Do not create new single-file task contracts such as `Tasks/T008-title.md`, and do not create a separate task-resolution directory or parallel task-storage convention for new work.

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
