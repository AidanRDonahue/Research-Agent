---
name: restructure-research-roadmap
description: Reorganize an existing Research-Agent project's roadmap and task relationships without solving the research itself. Use when the user asks to change a task's central question, split or merge research directions, change a task between root and child status, reparent a child task, add or remove dependencies or cross-links, turn an emerging result into a separate task, reorganize branches, or reconcile roadmap structure with the research that actually occurred. Preserve stable task identity, history, negative and inconclusive branches, and project-local rules from the current AGENTS.md.
---

# Restructure Research Roadmap

Change the structure of an existing research map while preserving scientific meaning, task identity, and research history.

## Workflow

1. Ground the operation in the target project.
   - Verify the repository and current default branch.
   - Read the current project `AGENTS.md` before interpreting or changing project state.
   - Read `dictionary.md` when notation or terminology may be affected.
   - Read the canonical structured roadmap, its human-readable projection, and the affected task artifacts.
   - Load only the affected tasks, their conceptual parents when present, dependencies, required cross-links, and directly relevant evidence unless a project-wide invariant requires more.

2. Classify the requested structural change.
   - central-question or scope change;
   - split one direction into multiple tasks;
   - merge or consolidate overlapping directions;
   - change a roadmap task between root and child status;
   - conceptual reparenting of a child task;
   - dependency or cross-link change;
   - promote an emerging result or obstruction into a new task;
   - archive, defer, or preserve a branch that no longer belongs in the primary line of attack;
   - broader roadmap reorganization.

3. Preserve identity and history.
   - Keep stable task IDs unless the project explicitly authorizes a different rule.
   - Do not renumber tasks for presentation convenience.
   - Preserve negative, inconclusive, abandoned, and superseded directions according to project history conventions rather than deleting them silently.
   - Keep lifecycle status separate from scientific outcome.
   - Keep `T001` as the special central research task outside the Mermaid roadmap graph.

4. Analyze semantic consequences before writing.
   - Identify which task questions, root/child classifications, parent relations, dependency edges, cross-links, task-folder text, roadmap entries, Mermaid links, and history records must change.
   - Check whether the proposed structure changes the mathematical meaning or evidentiary role of an existing task.
   - If a task's question changes materially, preserve the old research record and make the change explicit rather than rewriting history as though the old question never existed.
   - If splitting a task, allocate new task identities according to project rules and make the distribution of existing evidence explicit.

5. Present the proposed restructuring before mutation when meaning or dependency semantics change.
   - State the before/after root/child relationships and conceptual parents where applicable.
   - State which files will change.
   - Flag any identity, evidence, or historical ambiguity requiring user authority.
   - If the user's request already specifies the exact structural changes and project rules resolve all remaining details, proceed without redundant confirmation.

6. Apply the smallest coherent repository change.
   - Use the project's canonical roadmap source as the state authority.
   - Synchronize the Mermaid or human-readable projection.
   - Keep the central research question outside the Mermaid block and keep `T001` out of the Mermaid graph.
   - Make every Mermaid task node a clickable hyperlink to that task's canonical GitHub folder, updating the link whenever a canonical folder path changes.
   - Update affected task contracts only where their scope or relationships actually changed.
   - For a roadmap root, remove any conceptual parent; for a child, record exactly one existing conceptual parent. Do not use `T001` as a roadmap parent.
   - Create new task folders only when the restructuring genuinely introduces new tasks and the user has authorized that outcome.
   - Keep task-specific evidence with its task and genuinely global background inside the canonical `T001` folder.
   - Append history only as required by the project contract; never rewrite append-only history.

7. Validate the new structure.
   - Verify unique stable IDs.
   - Verify every roadmap task other than `T001` is classified as root or child.
   - Verify roots have no conceptual parent and children have exactly one existing conceptual parent other than `T001`.
   - Verify `T001` is absent from the Mermaid graph.
   - Verify parent and dependency graphs are acyclic.
   - Verify dependency and cross-link targets exist.
   - Verify every Mermaid task node has a clickable GitHub link to its corresponding canonical task folder.
   - Verify roadmap/task agreement on title, scope, root/child role, parent when applicable, dependencies, status, and deliverable paths where applicable.
   - Verify every moved or split evidence reference still points to an existing artifact and has a truthful evidentiary role.
   - Run project validators or CI when available and applicable.

8. Publish through the repository's required review workflow.
   - Prefer a scoped branch and reviewable pull request unless the user or project explicitly authorizes another path.
   - Report changed relationships, changed files, validation, and unresolved warnings.

## Boundaries

- Do not solve affected research questions as part of restructuring.
- Do not mark tasks complete merely because their roadmap role changed.
- Do not rewrite evidence to fit a preferred narrative.
- Do not silently erase an inconvenient branch or negative result.
- Do not prewrite future solution branches that have not arisen from user-directed research.
- Keep the roadmap a map of actual research decisions, not a retrospective fiction or a predetermined solution plan.
