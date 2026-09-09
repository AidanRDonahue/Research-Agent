# Lean Formalization System Checklist

Apply this checklist only when the project has initialized the optional Lean formalization layer. Project-local `AGENTS.md` remains authoritative if it replaces or narrows a rule.

## Workspace

- `lean-toolchain` exists and records the intended toolchain.
- A valid `lakefile.toml` or `lakefile.lean` defines the formalization workspace.
- `lake-manifest.json` is tracked after dependency resolution.
- Generated `.lake/` build state is not committed unless project rules explicitly require otherwise.
- `Formalization/README.md` explains the non-authoritative validation role of the Lean layer.
- `Formalization/result-map.yaml` is syntactically valid and uses the current mapping schema.

## Mapping integrity

- Every mapped task and result node exists in current Research-Agent state.
- Every mapped source path exists.
- Every mapped Lean module and declaration exists.
- Mapped project-result dependencies agree with actual formal imports/uses where applicable.
- Validation-report paths point to the corresponding task-local `Validation/lean-validation.md` file.
- The mapping does not contain task lifecycle status or purport to override research state.

## Translation integrity

- The validation report freezes the exact source claim.
- Domains, hypotheses, quantifiers, definitions, normalization, and conclusion are compared explicitly.
- Any stronger hypothesis, narrower domain, omitted case, or altered notion of equality/equivalence is disclosed.
- A qualified or blocked translation is not reported as faithfully kernel-verified.

## Machine validation

- The target module passes the applicable direct Lean check.
- The applicable Lake build succeeds.
- `#print axioms` (or an equivalent transitive axiom audit) has been run for the mapped declaration.
- `sorryAx` is absent for a `kernel-verified` verdict.
- Any axiom or trust dependency beyond `propext`, `Classical.choice`, and `Quot.sound` is surfaced and assessed.
- Imported mapped project results were validated at the scope in which they are used.

## Staleness

Revalidate when the source result, mapped dependency, Lean declaration, imported formalization, `lean-toolchain`, or `lake-manifest.json` changes materially.

## Reporting

State what passed, what failed, what could not be checked, and whether the current formalization is faithful, qualified, blocked, failed, inconclusive, or stale. Do not infer task completion from Lean validation.
