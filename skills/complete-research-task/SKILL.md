---
name: complete-research-task
description: Evaluate and complete an existing Research-Agent task when the user explicitly asks to resolve, complete, synthesize, or mark the task complete. Verify declared premises and evidence, write the canonical self-contained resolution at the supported scope, update the task result graph and lifecycle metadata, synchronize the roadmap/history, and validate without rewriting the original question to fit partial results.
---

# Complete Research Task

Use this workflow only for an explicit completion request. Evidence appearing sufficient is not, by itself, permission to complete the task.

## Establish authority and scope

1. Read the project's current `AGENTS.md` and `dictionary.md`.
2. Read the target `task-graph.md`, current `resolution.md`, declared parent, declared dependencies, required cross-links, and the task-local evidence needed to evaluate the original question.
3. Preserve the exact original task question and scope. Do not silently weaken or rewrite it to fit the available result.

## Completion gate

Before changing lifecycle state:

- verify every required premise/result is established or explicitly accounted for;
- distinguish success, negative, and inconclusive outcomes;
- verify cited or task-local evidence exists;
- audit assumptions, edge cases, notation, and dependency use;
- for formal mathematical claims, verify the proof at the exact claimed scope; and
- if the project requires a standardness/novelty audit for a proposed mathematical result, perform it and surface any user-authority decision before mislabeling a standard consequence as a new result.

If the evidence does not support completion, do not manufacture a resolution. Report the exact obstruction and keep the task pending unless project rules define an explicit completed-inconclusive state that the user requested.

## Write the resolution

When completion is supported:

1. Write `resolution.md` as the canonical self-contained completion record.
2. For theorem-like claims, include the full proof or exact certificate required by project rules.
3. For negative results, include the counterexample, failure certificate, experiment, or other decisive evidence.
4. For inconclusive outcomes, state the exact obstruction and the strongest established partial result.
5. Update `task-graph.md` so the task-local result-dependency graph reflects the actual evidence path to the conclusion.
6. Record completion metadata and keep lifecycle status separate from scientific or technical outcome.
7. Synchronize `roadmap.yaml` and `ROADMAP.md`, preserving a `click` directive for every Mermaid task node that links to that task's canonical GitHub folder.
8. Preserve `Tasks/T001-<root-slug>/Background/` as the canonical project-global background location; completion does not authorize relocating shared material to a top-level `Background/` directory.
9. Append required history without rewriting prior history entries.
10. Run the strongest applicable project validation and post-write review, including roadmap-link and global-background invariants.
11. Publish through the repository's required branch/review workflow.

## Boundaries

- Do not infer completion from a suggestive filename, summary, roadmap status, or partial proof.
- Do not silently discard negative or inconclusive evidence.
- Do not add new research branches during completion unless the user separately authorizes them.
