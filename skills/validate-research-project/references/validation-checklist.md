# Validation Checklist

Use this as a reusable baseline when the current project `AGENTS.md` does not replace or narrow a rule.

## Canonical structure

- Required project files and directories exist.
- `README.md` accurately describes project purpose, scope, structure, and working method.
- `AGENTS.md` defines project-local authority and rules without depending on a manual procedural module-routing table.
- `dictionary.md` is the canonical terminology and notation authority.
- `roadmap.yaml` is the canonical structured roadmap state.
- `ROADMAP.md` is a valid projection of `roadmap.yaml`: it states the central research question outside the Mermaid block, omits `T001` from the Mermaid graph, and every Mermaid task node links to the corresponding canonical GitHub task folder.
- `templates/`, `history/`, and `checks/` contain the project-defined canonical files.

## Roadmap integrity

- Stable IDs are unique, valid, monotone, and never reused.
- New display indices follow the current project default.
- `T001` is the central research task, has no conceptual parent, and does not appear as a node in the Mermaid roadmap graph.
- Every roadmap task other than `T001` is explicitly classified as a root node or child node.
- Root nodes have no conceptual parent.
- Child nodes have exactly one existing conceptual parent, and `T001` is not used as that parent.
- Parent and dependency graphs are acyclic.
- Dependency and cross-link targets exist and use stable IDs.
- Roadmap folder paths match actual canonical task folders.
- Every Mermaid task node is clickable and targets the GitHub location of the corresponding canonical task folder.

## Task integrity

- Every roadmap item has exactly one canonical `Tasks/<ID>-<slug>/` folder.
- Every task folder contains `task-graph.md` and `resolution.md`.
- Task contracts contain the project-required metadata, objective, scope, method, stopping rules, outcome branches, assumptions, conventions, validation, and result graph.
- Task contracts record roadmap role; conceptual-parent fields are present only for child nodes.
- Result-graph nodes and edges describe actual evidence/result dependencies rather than generic workflow steps.
- Every material evidence file/result required by a completed resolution lies on an explicit evidentiary path to the conclusion when project rules require that representation.
- Pending resolutions clearly remain pending and do not assert completed outcomes.
- Completed tasks contain self-contained resolutions at the exact supported scope.

## Evidence and history

- Referenced evidence exists at the recorded path.
- Task-specific evidence remains task-local.
- Genuinely global background material is stored inside the canonical `T001` task folder, normally under `background/`, rather than in a separate top-level background directory.
- Roadmap metadata is not treated as independent proof.
- `history/roadmap-events.jsonl` remains valid append-only JSONL when the project uses it.

## Mathematical review

For project-authored mathematics changed by the operation:

- notation agrees with `dictionary.md`;
- statements and proofs agree;
- assumptions, quantifiers, domains, edge cases, dimensions, signs, indices, and normalization are checked;
- named operations use the project's required typesetting convention;
- cited or dependency results are used only at established scope; and
- proposed new results receive the project's required standardness/novelty review.

## Reporting

State which checks were run, what passed, what failed, what could not be verified, and any repository-specific validator limitations. Do not report a retired or incompatible validator as passing the current project layout.
