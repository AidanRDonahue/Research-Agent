---
name: formalize-result-with-lean
description: Translate one bounded mathematical result from a Research-Agent project into Lean 4 and validate the formalization as an independent proof certificate. Use when the user explicitly asks to formalize a Research-Agent result in Lean, machine-check a result with Lean, initialize the project's optional Lean formalization layer, repair an existing Lean formalization, or revalidate it after source, dependency, or toolchain changes. Preserve the exact source claim and project authority, audit translation fidelity, dependencies, builds, and axioms, and never infer task completion or change roadmap/lifecycle state merely from a Lean verdict.
---

# Formalize Result with Lean

Treat Lean formalization as an independent validation artifact. Keep the Research-Agent project authoritative for what the research claim means.

Do not equate successful Lean elaboration with validation of the natural-language claim until translation fidelity has been established separately.

Use the templates in `assets/` when initializing the optional Lean layer or creating a task-local validation report. Read `references/validation-contract.md` before writing `result-map.yaml` or assigning a verdict.

## Workflow

1. Establish project authority and target scope.
2. Choose exactly one operation: initialize, formalize, repair, or revalidate.
3. Freeze the exact source claim.
4. Construct and audit the Lean translation.
5. Formalize only the bounded result and required dependencies.
6. Run Lean validation and inspect transitive axioms.
7. Compare the checked Lean declaration with the frozen source claim.
8. Assign exactly one validation verdict.
9. Record the mapping and validation report only when writes are authorized.
10. Verify repository writes and run applicable project checks.

## Establish authority and scope

1. Verify the repository and current default branch.
2. Read the current project `AGENTS.md` before interpreting or changing project state.
3. Read `dictionary.md` before translating mathematical notation or terminology.
4. Read the target task's `task-graph.md`, the exact result node under review, and only the resolution, evidence, dependencies, and cross-links required to understand that result.
5. Read existing Lean workspace files when present: `lean-toolchain`, `lakefile.toml` or `lakefile.lean`, `lake-manifest.json`, `Formalization/result-map.yaml`, the target result module, and directly imported project-result modules.
6. Treat `roadmap.yaml` and `ROADMAP.md` as research-navigation state, not mathematical proof sources.
7. Before a Skill-driven repository mutation, compare `research-agent.lock.json` with concrete installed distribution metadata when both are available. Surface a mismatch rather than silently treating different tooling as compatible.

Do not load unrelated roadmap branches merely because they contain mathematics.

## Choose the operation

Use one bounded operation:

- **initialize** — create the optional Lean formalization layer;
- **formalize** — translate and prove one identified result node;
- **repair** — correct an existing formalization or proof;
- **revalidate** — rerun fidelity and machine checks on an existing mapping.

Do not initialize or modify files merely because Lean validation might be useful. Require an explicit request to initialize, formalize, repair, or revalidate before writing.

## Initialize the Lean layer

When initialization is explicitly requested and the project does not already define another Lean layout, create this default structure:

```text
<Project>/
|-- lean-toolchain
|-- lakefile.toml
|-- lake-manifest.json              # after dependency resolution
|-- Formalization/
|   |-- README.md
|   |-- result-map.yaml
|   `-- ResearchFormalization/
|       `-- Common/
|           `-- Definitions.lean
|-- templates/
|   `-- lean-validation.md
`-- checks/
    `-- lean-system-checklist.md
```

Copy the corresponding files from `assets/`. Create `lean-toolchain` from the actual resolved toolchain rather than from a guessed version. Use `assets/lakefile.toml` only when the project does not already have a Lake configuration; adapt it narrowly if the project needs Mathlib or another declared dependency, then resolve dependencies so Lake generates `lake-manifest.json`.

Add task-specific files only when an actual result is formalized:

```text
Formalization/ResearchFormalization/Tasks/T004/R003.lean
Tasks/T004-<slug>/Validation/lean-validation.md
```

Preserve these rules:

- Keep Lean modules separate from human-friendly task folder slugs.
- Use `ResearchFormalization` as the default Lean library/module root unless the project already establishes another convention.
- Do not pre-create result modules for hypothetical or future result nodes.
- Put genuinely shared formal definitions in `Common/`; keep task-specific definitions in the corresponding task/result module.
- Do not move research evidence into `Formalization/`.
- Ensure generated `.lake/` build state is ignored according to project conventions.
- Keep `lake-manifest.json` under version control when generated.
- Do not guess Lean, Mathlib, or dependency versions from model memory.
- Use Mathlib when required by the mathematics; do not introduce it merely by default if core Lean suffices.
- Do not overwrite an existing Lean workspace without explicit authorization.
- Add the Lean system checklist to the project's structural validation path when the optional layer is initialized.

## Freeze the source claim

Before writing Lean, record the exact mathematical claim being translated:

- task stable ID and result-node identifier;
- source file and source revision or fingerprint;
- hypotheses;
- domains and types;
- quantifiers;
- definitions and notation;
- normalization conventions;
- conclusion;
- cited project-result dependencies;
- relevant edge or degenerate cases.

Distinguish the theorem-level claim from motivation, examples, heuristics, numerical observations, and surrounding exposition.

Do not silently repair an ambiguous or false-looking source statement while formalizing it.

## Construct the translation contract

Map every material source construct to its Lean representation. Check explicitly for changed quantifier order, implicit versus explicit hypotheses, strengthened assumptions, narrowed domains, omitted side conditions, altered equality or equivalence notions, finite versus infinite cases, exact versus approximate statements, existence versus witness requirements, normalization changes, coercions and subtype restrictions, and hidden nonemptiness, decidability, finiteness, regularity, or choice assumptions.

Classify translation fidelity before treating a proof as validation:

- **faithful** — the Lean declaration expresses the source claim at the same mathematical scope;
- **qualified** — Lean expresses a useful but stronger-hypothesis, narrower, or otherwise modified statement;
- **blocked** — ambiguity or missing definitions prevent a defensible translation.

If translation is blocked, stop the proof-validation path and report the exact obstruction. Do not hide a qualified translation behind a successful Lean build.

## Handle dependencies

For a source hypothesis, encode it as a Lean parameter or hypothesis when that preserves the source statement.

For a prior project result, import and use its mapped Lean declaration when an applicable formalization exists, verify that it applies at the required scope, and preserve the dependency relationship in `result-map.yaml`.

Do not introduce an `axiom` merely to make an unformalized project result available.

If a required project result lacks an adequate Lean certificate, either stop and report the unresolved dependency, or—when the user explicitly authorizes a conditional formalization—expose the extra assumption and classify the final verdict as qualified.

Never call a downstream source claim kernel-verified when its proof relies on a stronger assumption that is not part of the source claim.

## Write the Lean formalization

Use the default path:

```text
Formalization/ResearchFormalization/Tasks/<TASK-ID>/<RESULT-NODE>.lean
```

Use module names such as `ResearchFormalization.Tasks.T004.R003` and prefer one primary declaration corresponding to the mapped result node.

Keep the theorem statement visually separate from proof implementation so translation review can inspect the declaration independently of tactics. Use imports that reflect actual formal dependencies.

Do not use `sorry`, `admit`, project-specific unproved `axiom` declarations, or hidden assumptions to obtain a final verified verdict. Automation and tactics are allowed when they produce a proof accepted by Lean and do not introduce an undisclosed trust dependency.

Do not refactor unrelated Lean modules during a bounded formalization.

## Validate with Lean

Use the repository's pinned Lean/Lake environment. Run the strongest applicable direct target check, normally:

```text
lake lean <target-file>
```

Then run the applicable package build, normally:

```text
lake build
```

Do not update package versions during ordinary validation.

A successful build is necessary but not sufficient. Audit the target declaration's transitive axioms with `#print axioms <declaration>` in an audit module or equivalent Lean invocation.

Reject an unqualified `kernel-verified` verdict if the target depends on `sorryAx`. By default, treat `propext`, `Classical.choice`, and `Quot.sound` as the standard benign axioms of Lean's logic. Surface every other reported axiom or trust dependency explicitly and investigate its origin before deciding whether anything stronger than a qualified verdict is justified.

Record the Lean toolchain, dependency manifest revision or fingerprint when available, target module, target declaration, direct-check result, full-build result, transitive axioms, source revision, and dependency formalizations used.

Do not interpret a Lean compiler or tactic failure as evidence that the mathematical claim is false.

## Compare the checked declaration with the source

After the proof checks, compare the elaborated Lean declaration with the frozen source claim again. Verify that all source hypotheses remain present and no stronger ones appeared, domains and quantifiers agree, definitions agree, the conclusion has not weakened, imported project results were used only at their established scope, and no unresolved translation qualification remains.

Successful proof search does not override a translation mismatch.

## Verdict

Use exactly one primary verdict:

- **kernel-verified** — the translation is faithful, the declaration checks, the applicable build succeeds, no incomplete proof dependency is present, and no unapproved axiom or unresolved project-result dependency remains;
- **lean-checked-with-qualifications** — Lean checks the declaration, but the translation is narrower or stronger, an additional assumption or trust dependency remains, or another disclosed qualification prevents exact validation of the source claim;
- **translation-blocked** — ambiguity, undefined constructs, or unresolved semantic choices prevent a faithful formalization;
- **proof-failed** — an adequate formal statement was constructed but the Lean proof or build does not check;
- **inconclusive** — the required Lean environment, dependency state, source context, or validation capability is unavailable;
- **stale** — a prior Lean validation exists but its source claim, mapped dependencies, Lean module, toolchain, or dependency manifest has materially changed.

Do not use `kernel-verified` merely because `lake build` succeeds.

## Record formalization state

When repository writes are authorized, maintain `Formalization/result-map.yaml` as a machine-readable index between research result nodes and Lean declarations. Do not make the mapping file a source of mathematical truth.

Record at least the task stable ID, result-node identifier, source path, source revision or fingerprint, Lean module, Lean declaration, mapped project-result dependencies, and task-local validation-report path.

Write the human-readable validation result to `Tasks/<TASK-ID>-<slug>/Validation/lean-validation.md` using `assets/lean-validation.md` and the contract in `references/validation-contract.md`.

Keep the formalization verdict separate from task lifecycle and research outcome.

## Detect staleness

Treat an existing validation as potentially stale when the source result statement, its assumptions or definitions, a mapped project-result dependency, the target Lean theorem statement, imported project formalizations, `lean-toolchain`, or `lake-manifest.json` changes materially.

Revalidate rather than carrying forward an old verdict by assumption.

## Repository writes

For substantive repository mutations:

1. Use a scoped branch unless the user explicitly authorizes another path.
2. Write only the formalization and validation artifacts required by the requested operation.
3. Reread or otherwise verify every saved artifact.
4. Rerun the target Lean check and applicable package build.
5. Run the project's strongest applicable structural validation, including `checks/lean-system-checklist.md` when present.
6. Open a reviewable pull request when supported by the project workflow.

Do not modify the default branch directly unless explicitly authorized.

## Boundaries

- Do not change `roadmap.yaml`, `ROADMAP.md`, task status, lifecycle state, completion metadata, or roadmap history merely because Lean validation succeeds or fails.
- Do not mark a research task complete.
- Do not rewrite the natural-language research claim to match an easier Lean theorem.
- Do not silently strengthen assumptions.
- Do not treat roadmap metadata as mathematical evidence.
- Do not promote task-specific formal definitions into `Common/` merely for convenience.
- Do not update Lean or Mathlib versions during an ordinary result validation.
- Do not call an incomplete or qualified formalization kernel-verified.
- Do not treat lack of a Lean proof as refutation of the source theorem.
- Surface exact translation failures, proof failures, trust dependencies, and tooling limitations.
