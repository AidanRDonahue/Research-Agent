---
name: review-mathematical-result
description: Audit one mathematical claim, proof, derivation, bound, or argument adversarially. Use when the user asks to scrutinize a result, find gaps or counterexamples, verify that a proof establishes the theorem exactly as stated, identify hidden assumptions, compare the proved scope with the claimed scope, repair a false or incomplete statement, or assess whether a result is standard, routine, a reformulation, or plausibly project-specific. When repository context is involved, respect the current project AGENTS.md and dictionary.md.
---

# Review Mathematical Result

Examine one bounded mathematical result as a skeptical referee. Preserve the distinction between reviewing a result and changing project state.

## Workflow

1. Ground the review.
   - If the result belongs to a repository, verify the target repository and read its current `AGENTS.md` first.
   - Read `dictionary.md` when present before interpreting notation.
   - Load the target task, the result under review, and only the dependencies or evidence needed to test it.
   - Otherwise use the exact statement, proof, derivation, or notes supplied by the user.

2. Freeze the exact claim before judging the proof.
   - State the hypotheses, domains, quantifiers, normalization, and conclusion precisely.
   - Separate the theorem-level claim from motivation, examples, heuristics, or implementation observations.
   - Identify what must be proved for the claim to hold at the stated scope.

3. Audit dependencies.
   - Identify every nontrivial earlier result used.
   - Check that each dependency applies under the present hypotheses.
   - Look for circular reasoning, imported assumptions, strengthened premises, and unproved existence or regularity conditions.

4. Audit the argument line by line at the level needed for correctness.
   - Test implications, equivalences, case splits, substitutions, limit operations, expectations, inverses, rank assumptions, sign conditions, dimensions, domains, and equality cases when relevant.
   - Distinguish a missing explanation from a genuine logical gap.
   - Do not accept a conclusion merely because it is plausible or familiar.

5. Search actively for failure modes.
   - Try simple examples and smallest nontrivial cases.
   - Test boundary, degenerate, singular, symmetric, low-dimensional, and pathological cases when meaningful.
   - Reverse-engineer the weakest step and try to violate its hidden assumptions.
   - Use exact or computational checks when they materially test the claim and the necessary tools are available.

6. Compare claim scope with proved scope.
   - Record the claim as written.
   - Record the strongest statement actually established by the argument.
   - If they differ, identify the exact lost hypothesis, missing case, or overstatement.
   - When repair is possible, give only the strongest repaired claim justified by the evidence.

7. Assess standardness when the user asks about novelty, originality, or whether a result is already known.
   - Distinguish known theorem, routine corollary, straightforward reformulation, project-specific specialization, and genuinely uncertain status.
   - Search appropriate current literature or public sources when access is available and the classification matters.
   - Never treat absence from the project repository as evidence of novelty.
   - Do not claim novelty without adequate external support.

## Verdict

Use exactly one primary verdict:

- **verified** — the argument supports the stated claim at its exact scope;
- **verified with qualifications** — the core result is correct but requires explicit qualifications, missing routine details, or narrower wording;
- **gap found** — a material proof obligation is not established, but the claim has not been disproved;
- **false** — a counterexample or contradiction refutes the stated claim;
- **inconclusive** — available evidence is insufficient to decide.

Report, in this order:

1. verdict;
2. exact claim reviewed;
3. strongest findings, with failures first;
4. dependency and edge-case findings;
5. claim-as-written versus claim-actually-proved;
6. strongest defensible repair, if needed;
7. standardness assessment, only when relevant;
8. unresolved questions.

## Boundaries

- Do not rewrite the proof unless the user asks for a corrected proof or exposition.
- Do not transcribe the result into evidence automatically.
- Do not modify `task-graph.md`, `resolution.md`, roadmap state, lifecycle state, history, or `dictionary.md` merely because the review reached a verdict.
- Do not mark a task complete.
- Do not silently change notation to avoid a conflict; surface project-authority conflicts when they matter.
- Do not broaden the claim during repair.
