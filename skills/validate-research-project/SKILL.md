---
name: validate-research-project
description: Audit a Research-Agent project or a proposed repository change for structural, roadmap, task, evidence, terminology, history, and applicable mathematical consistency. Use when the user asks to validate, audit, check, review, verify, or scrutinize a research project/change before publishing or completion. Report failures and limitations explicitly rather than repairing them unless repair is also requested.
---

# Validate Research Project

Validate against the target repository's current authorities rather than a remembered schema.

## Procedure

1. Read the current project `AGENTS.md` first.
2. Read `checks/project-system-checklist.md` and any repository-specific validators or CI instructions it names.
3. Inspect only enough repository state to evaluate the requested validation scope, expanding to project-wide checks when the user requests a full audit or when structural invariants require it.
4. Apply the checklist in `references/validation-checklist.md` only where it is consistent with current project-local instructions. Project-local rules control conflicts.
5. Run available deterministic validators or tests when applicable.
6. For mathematical material written or revised in the validated change, audit statement/proof consistency, notation, assumptions, quantifiers, edge cases, and dependence on earlier results.
7. For proposed new mathematical results, assess whether they appear to be standard consequences, routine corollaries, or reformulations rather than treating absence from the repository as evidence of novelty.
8. Report failures, warnings, uncertainty, and validation limitations explicitly.

## Repair boundary

Validation is an audit. Do not mutate the repository merely because a check failed unless the user also requested repair. When a repair is requested, keep it scoped to the identified failure and revalidate afterward.
