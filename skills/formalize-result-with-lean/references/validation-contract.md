# Lean Formalization Validation Contract

Use this reference to keep Research-Agent result mappings and task-local Lean validation reports consistent.

## Result map

Use `Formalization/result-map.yaml` only as an index between research result nodes and Lean declarations. It is not a source of mathematical truth or task lifecycle state.

Each entry must contain:

- task stable ID;
- result-node identifier;
- source path;
- source revision or fingerprint;
- Lean module;
- Lean declaration;
- mapped project-result dependencies;
- task-local validation-report path.

Use `assets/result-map.yaml` as the initialization template.

## Translation fidelity

Classify the translation independently of proof success:

- **faithful** — the Lean declaration expresses the source claim at the same mathematical scope;
- **qualified** — the Lean declaration is useful but narrower, stronger in hypotheses, or otherwise modified;
- **blocked** — ambiguity or missing definitions prevent a defensible translation.

A proof of a qualified declaration does not validate the original source claim exactly.

## Machine validation

For the mapped declaration, record:

- Lean toolchain;
- Lake manifest revision or fingerprint when available;
- direct target check result;
- full build result;
- transitive axioms from `#print axioms`;
- imported mapped result declarations.

Treat `sorryAx` as an incomplete proof dependency. By default, `propext`, `Classical.choice`, and `Quot.sound` are acceptable standard axioms. Surface other axioms or trust dependencies explicitly and investigate them before issuing an unqualified verdict.

## Verdicts

Use exactly one:

- **kernel-verified** — faithful translation, successful checks/build, no incomplete proof dependency, no unresolved mapped dependency, and no unapproved trust dependency;
- **lean-checked-with-qualifications** — Lean checks the encoded declaration, but a translation, assumption, dependency, or trust qualification prevents exact validation of the source claim;
- **translation-blocked** — the source cannot yet be represented faithfully;
- **proof-failed** — the formal statement is adequate but the Lean proof or build does not check;
- **inconclusive** — tooling, dependency, source, or environment limitations prevent a meaningful verdict;
- **stale** — an earlier validation no longer matches the current source or formal environment.

A proof failure is not a mathematical counterexample.

## Report requirements

Use `assets/lean-validation.md` for `Tasks/<TASK-ID>-<slug>/Validation/lean-validation.md`.

The report must state exactly what Lean establishes and whether that declaration matches the source claim at its original scope. Never collapse a qualified translation into `kernel-verified`.
