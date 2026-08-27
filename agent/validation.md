# Validation

## Project validation

`checks/project-system-checklist.md` defines the manual or automated project-system validation procedure.

Repository validators, scripts, or CI checks may extend this validation, but they must remain consistent with the invariants defined in this file.

## Post-write mathematical review

Whenever mathematical material is written or revised in the repository, review the saved mathematics before reporting the write complete. The review must be scoped to what was written and is not authorization to continue the research program beyond the user's request.

For any proposed new theorem, lemma, proposition, identity, derivation, or other mathematical result in the written material:

- audit the proof or derivation for correctness at the exact claimed scope, including assumptions, quantifiers, edge cases, notation consistency, and dependence on earlier results;
- determine whether the result is genuinely new within the project context or instead appears to be a direct instance, routine corollary, reformulation, or standard consequence of results a field expert would ordinarily regard as established background;
- do not treat absence from the repository as evidence of mathematical novelty;
- if the result appears standard or derivative in this sense, explain the basis for that assessment and bring the issue to the user's attention rather than silently presenting it as a new project result; and
- ask how the user wants to reconcile that finding, for example by citing the standard result, reframing the project statement as a corollary or specialization, retaining the proof as self-contained exposition, or taking another user-selected action.

If the standardness determination is uncertain, state that uncertainty explicitly and ask the user before changing the claimed status of the result. Do not silently delete, downgrade, or relabel a proposed result without the user's direction.

For mathematical material that does not propose a new result, still verify notation, statement/proof consistency, and obvious mathematical errors before reporting the repository write complete.

## Validation gate

Before publishing project-system, task, or roadmap changes, verify:

- all mandated top-level files and directories exist;
- `README.md` documents project purpose, scope, repository structure, and working procedure;
- `AGENTS.md` defines the core mandate and module routing;
- all routed files in `agent/` exist, supporting modules do not define module-routing rules, and the current action can be resolved from the `AGENTS.md` routing table;
- `dictionary.md` defines canonical terminology, identifiers, naming conventions, and domain-specific definitions;
- `roadmap.yaml` remains the canonical project-state source;
- `ROADMAP.md` is a valid human-readable or visual projection of `roadmap.yaml`;
- every roadmap item links to its canonical work folder;
- stable IDs are unique, valid, and not reused;
- display indices, when used, are unique and consistent with the conceptual tree, and newly created items default their `display_index` to the stable ID unless the user or an existing project convention specifies otherwise;
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
- mathematical repository writes have received the required post-write mathematical review, including the standardness audit for proposed new results;
- supporting evidence referenced by a resolution exists in the same task folder or is an explicitly shared foundation in `Background/`;
- the canonical files in `templates/` exist and are used for new work items;
- `roadmap.yaml` agrees with task folders and completion artifacts;
- history remains valid append-only JSONL in `history/roadmap-events.jsonl`;
- `checks/project-system-checklist.md` exists and remains consistent with current project-system requirements;
- repository terminology and conventions are preserved; and
- project-specific artifacts do not replace, duplicate, or contradict the canonical project-system structure.

If an available validator assumes a retired repository or task layout, do not report it as passing the current layout. Perform the strongest available manual or migration-specific structural validation and state that limitation explicitly.

After a successful mutation, report project state, files changed, branch, commit(s), draft pull request, validation performed, and unresolved warnings.
