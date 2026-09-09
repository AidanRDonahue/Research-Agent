# Formalization

This directory contains optional Lean 4 formalizations used as independent validation artifacts for Research-Agent result nodes.

Research state remains authoritative in the project's normal Research-Agent files. A successful Lean proof certifies the mapped Lean declaration; it validates the natural-language research result only when the task-local validation report also establishes faithful translation.

## Layout

```text
Formalization/
|-- README.md
|-- result-map.yaml
`-- ResearchFormalization/
    |-- Common/
    |   `-- Definitions.lean
    `-- Tasks/
        `-- <TASK-ID>/
            `-- <RESULT-NODE>.lean
```

`result-map.yaml` indexes research result nodes to Lean declarations. It is not evidence, roadmap state, or task lifecycle state.

Keep genuinely shared formal definitions in `Common/`. Keep result-specific assumptions and constructions with the corresponding task/result module.

Do not treat a passing `lake build` by itself as proof that the natural-language source claim was validated. Consult the task-local `Validation/lean-validation.md` report for translation fidelity, dependencies, transitive axioms, and the final Lean-validation verdict.
