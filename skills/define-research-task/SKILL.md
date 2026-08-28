---
name: define-research-task
description: Define and publish a new bounded research task in an existing Research-Agent project. Use when the user asks to define, create, add, or branch a research task/node. Conduct guided intake before writing, then create the canonical task folder, task contract, pending resolution, roadmap updates, and required history without autonomously solving the task.
---

# Define Research Task

Create a new task only after its bounded research contract is clear.

## Start with project authority

1. Verify the exact project repository and read its current `AGENTS.md`.
2. Read `dictionary.md`, the current roadmap state, and only the parent/dependency/cross-link context needed to define the proposed task.
3. Do not ingest unrelated roadmap branches merely to create a task.

## Guided intake

Do not write repository files during intake.

Begin with:

> What concrete action and bounded target should this task have?

Gather one precise item at a time until the following are clear enough to publish without inventing research decisions:

- action-oriented title;
- type and initial lifecycle status;
- exactly one conceptual parent unless the task is the root;
- relation to parent and effect on parent;
- uncertainty reduced or question answered;
- declared dependencies and required cross-links;
- objective;
- bounded method or execution plan;
- stopping rules;
- success, negative, and realistic inconclusive branches;
- scope exclusions;
- assumptions and project conventions;
- independent validation standard; and
- planned task-local result-dependency graph.

The user may answer naturally. Translate their decisions into the project schema without forcing them to fill out a form.

## Publication

When the user authorizes creation:

1. Allocate the next unused stable ID according to project rules. Do not renumber existing IDs.
2. Default `display_index` to the stable ID unless the project or user specifies another value.
3. Create exactly one canonical `Tasks/<STABLE-ID>-<slug>/` folder.
4. Populate `task-graph.md` from the current project template.
5. Create or copy `resolution.md` with an explicit pending notice.
6. Put supplied task-specific sources or evidence in that same task folder.
7. Synchronize `roadmap.yaml` and `ROADMAP.md`.
8. Append project history only when required by the current project rules.
9. Validate the structural change before publishing it.
10. Use a scoped branch and reviewable pull request for substantive mutations unless the user explicitly authorizes another write path.

## Boundaries

- Defining a task does not authorize solving it.
- Do not prepopulate evidence with conclusions that have not been established.
- Do not create extra sibling or successor tasks merely because they appear useful.
- Keep the roadmap a map of actual research decisions, not a prewritten solution plan.
