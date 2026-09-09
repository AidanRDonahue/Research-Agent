# Lean validation — <TASK-ID>/<RESULT-NODE>

## Source

- Task: <TASK-ID>
- Result node: <RESULT-NODE>
- Source path: <PATH>
- Source revision/fingerprint: <REVISION>
- Exact claim: <CLAIM>

## Translation

- Lean module: <MODULE>
- Declaration: <DECLARATION>
- Fidelity: <faithful | qualified | blocked>

### Construct mapping

| Source construct | Lean representation | Status |
| --- | --- | --- |
| <construct> | <representation> | <exact | qualified | unresolved> |

### Translation qualifications

- <None, or exact discrepancies.>

## Dependencies

| Research dependency | Lean declaration | Validation state |
| --- | --- | --- |
| <dependency> | <declaration> | <state> |

## Machine validation

- Lean toolchain: <TOOLCHAIN>
- Lake manifest revision/fingerprint: <MANIFEST>
- Direct target check: <RESULT>
- Full build: <RESULT>
- Transitive axioms: <AXIOMS>

## Verdict

**<kernel-verified | lean-checked-with-qualifications | translation-blocked | proof-failed | inconclusive | stale>**

## Basis

<State exactly what Lean establishes and whether it validates the source claim at its original scope.>

## Limitations

<State every unresolved translation, dependency, trust, tooling, or reproducibility limitation.>
