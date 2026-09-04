# Paper Digest Taxonomy

Use three orthogonal axes for canonical semantic nodes: **kind**, **warrant/subtype**, and **story function**. Do not infer one axis from another.

## Kind

- `statement`: assertable proposition, observation, assumption, claim, theorem, limitation, or cited fact.
- `construct`: defined or built object such as a method, algorithm, representation, dataset, metric, or model.
- `target`: research question, desideratum, design goal, evaluation question, or open question.
- `proof`: proof container for one proved statement.
- `step`: one substantive move inside a proof.

## Statement warrant

- `cited`: supported externally by a cited source.
- `assumed`: taken as a premise or condition.
- `proved`: formally established in the paper.
- `derived`: derived in prose or algebra without a formal proof environment.
- `observed`: measured or directly seen in experiment/table/figure/data.
- `interpreted`: authorial inference or claim beyond the direct warrant.
- `conjectured`: hypothesized or expected.
- `bounded`: limitation, scope restriction, caveat, or failure mode.

## Target subtype

- `research_question`
- `desideratum`
- `design_goal`
- `evaluation_question`
- `open_question`

## Construct subtype

- `definition`
- `construction`
- `representation`
- `method`
- `algorithm`
- `model`
- `dataset`
- `metric`
- `baseline`

## Story function

Use one of:

`context`, `problem`, `motivation`, `goal`, `approach`, `setup`, `guarantee`, `evaluation`, `evidence`, `theory_answer`, `empirical_answer`, `interpretation`, `comparison`, `boundary`, `future`.

A target's story function normally follows its subtype: goals/desiderata are `goal`, evaluation questions are `evaluation`, and open questions are `future`.

## Relation types

- `refines`: target -> narrower target.
- `motivates`: problem/claim/goal -> target or construct.
- `answered_by`: target -> claim or construct.
- `develops`: claim -> claim, for narrative extension/synthesis.
- `requires`: assumption -> statement/construct.
- `uses`: construct or proved statement -> statement/construct/proof step.
- `entails`: statement -> statement, including step -> step.
- `supports`: cited/proved/derived/observed -> interpreted claim.
- `proves`: proof or terminal proof step -> proved statement.
- `qualifies`: bounded statement -> statement.
- `challenges`: statement -> statement or proof step.
- `contrasts`: statement <-> statement.
- `instantiates`: statement -> statement for a special case/example.

Every relation has `basis: explicit|inferred`. Explicit relations should include source anchors for the connective evidence. Inferred relations must be visibly marked as reconstruction by the digest author.

## Coverage assignments

Every in-scope source unit gets exactly one primary assignment:

- `home(N####)`
- `echo(N####)`
- `edge-evidence(R####)`
- `discard(<reason>)`
- `structure`

Allowed discard reasons:

`signpost`, `pointer`, `gloss`, `illustration`, `courtesy`, `artifact`, `declaration`, `duplicate`.

## Home rule

The canonical home of an idea should be its strongest substantive statement nearest the relevant warrant. Abstract, introduction, roadmap, and conclusion restatements are normally echoes of body nodes rather than new nodes.

## Interpreted vs observed

Use `observed` for statements that directly report measured or displayed evidence. Use `interpreted` when a reader could agree on the data but disagree with the authors' inference from it.

## Problem vs target

A problem is an assertable statement about a deficiency or obstacle; it is not a target kind. Connect it with `motivates` to the target that addresses it.

## Formal results and proofs

A theorem remains a `statement` with warrant `proved`. Its proof is a separate `proof` node and its substantive proof moves are `step` nodes. A defect inside a proof belongs on the affected proof/step, not as a silent relabeling of the theorem statement.
