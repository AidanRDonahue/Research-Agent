---
name: paper-digest
description: Digest one academic paper into a nested Markdown knowledge package inside an instantiated Research-Agent project's canonical Background directory. Use when the user supplies or identifies a paper by arXiv, DOI, URL, PDF, LaTeX, or Markdown and asks to digest, dissect, map, or preserve it for later research, including its inquiry tree, claims and warrants, constructs, theorem/proof structure, typed relations, and coverage ledger. Preserve source anchors, keep background distinct from established project results, and do not use Python, JSON, or HTML as the digest representation.
---

# Paper Digest

Turn one paper into a repository-native Markdown knowledge package. Preserve the useful discipline of a bottom-up paper dissection while presenting the result top-down through the paper's inquiry structure.

Do not create or execute Python for the digest. Do not use JSON or HTML as the canonical representation. The durable output is the Markdown tree described in [`references/output-layout.md`](references/output-layout.md).

This workflow adapts ideas from ZhengchaoW's `paper-dissect` project. See [`UPSTREAM_LICENSE.md`](UPSTREAM_LICENSE.md) for attribution and license terms.

## Required reads and target

1. Read the target project's current `AGENTS.md` before interpreting project state or writing anything.
2. Follow the project's declared background authority. Under the current Research-Agent baseline, project-global background belongs under the root task's canonical `Tasks/T001-<root-slug>/Background/` directory; do not invent a separate top-level `Background/` directory.
3. Read [`references/taxonomy.md`](references/taxonomy.md) completely before classifying paper content.
4. Read [`references/output-layout.md`](references/output-layout.md) completely before creating files.
5. Resolve one paper and one target project. If either required input is genuinely missing and cannot be resolved from the request or repository, ask only for that missing item.
6. If a digest for the same paper and version already exists, update the existing package in place rather than creating a second canonical copy. Preserve stable node IDs and paths where their meanings have not changed.

Treat paper digestion as a background-ingestion operation, not as task completion or acceptance of the paper's claims as project truth.

## Source intake

1. Establish the paper's bibliographic identity: title, authors, year, stable identifier, version/date when available, and source location.
2. Prefer the user's supplied source when it is authoritative for the requested version. Otherwise use the best available author/arXiv/venue source. If only a PDF is available, use the available PDF reading capability and record that the digest was PDF-derived.
3. Prefer source forms that preserve theorem environments, equation labels, figure/table labels, and section structure. Do not require a conversion script.
4. Record source provenance and extraction limitations in `metadata.md` before drawing conclusions from damaged or incomplete text.
5. Preserve mathematical notation faithfully. If extraction appears to damage a formula, inspect the original page/source rather than guessing.
6. Do not reproduce the full paper in the digest. Paraphrase semantic nodes and use precise section/page/theorem/figure/table anchors; quote only when a short quotation is materially necessary and permitted.

## Build the coverage ledger first

Read the paper in source order and define stable source units (`u0001`, `u0002`, ...). A unit is normally one sentence, a tightly coupled mathematical block, a theorem/proof environment boundary, a figure/table caption, or another smallest practical block whose role can be classified without destroying meaning.

Every material unit inside the declared digestion scope must receive exactly one primary assignment:

- **home** — the unit is the canonical source home of one node;
- **echo** — the unit restates a node whose home is elsewhere;
- **edge-evidence** — the unit primarily states or justifies a relation between nodes;
- **discard** — the unit is non-semantic discourse, with an explicit discard reason from the taxonomy; or
- **structure** — the unit is a heading, environment label, or other structural marker.

Do not select only apparently important sentences and ignore the remainder. When the same idea appears in the abstract, introduction, body, and conclusion, place its canonical home nearest the source warrant and mark the other occurrences as echoes.

The minimum normal scope is the complete main body plus complete proofs of the main theorems. If appendices, supplementary proofs, or other sections are not fully digested, list them explicitly as outside the dissected range in `coverage/README.md`; never imply complete coverage when it was not achieved.

## Create canonical semantic nodes

Create one canonical node for each distinct idea according to the taxonomy. Use stable generic IDs (`N0001`, `N0002`, ...) and short slugs. Do not encode story function into IDs.

For every node, record:

- kind;
- statement warrant or target/construct subtype;
- story function;
- one canonical source home;
- source anchors and echoes;
- concise source-faithful paraphrase;
- incoming and outgoing typed relations; and
- any extraction uncertainty, scope limitation, or unsupported interpretation.

Keep one node to one assertable statement, construct, target, proof, or proof step. Do not collapse an entire section into one node merely for convenience.

## Build typed relations

Record relations in `relations.md` using the vocabulary in the taxonomy. Mark each relation's basis as `explicit` when the authors state it and `inferred` when the digest reconstructs it.

Reserve `supports` for warrant-to-claim support. Use `develops` for claim-to-claim narrative development. Use `answered_by` for target-to-answer links, `refines` for target hierarchy, and `proves` for proof-to-formal-result links.

Attach a source anchor for explicit edge evidence. If an inferred relation is useful but not textually stated, say so; do not present inference as authorial wording.

## Build the inquiry storyline

Identify the paper's root research target even when it is expressed as criteria or desiderata rather than a literal question. Then:

1. connect narrower desiderata, design goals, evaluation questions, and open questions with `refines`;
2. connect each answered target to the claim or construct that answers it with `answered_by`;
3. leave a target unanswered only when the paper genuinely leaves it open or the current digestion scope cannot establish the answer;
4. connect later headline claims with `develops` when they extend or synthesize earlier claims; and
5. keep finer supporting claims below the headline claim rather than duplicating them as separate storyline headlines.

Mirror only the `refines` target hierarchy as nested folders under `storyline/`. Storyline files are navigation/projection files that link to canonical nodes; do not duplicate canonical semantic content there.

## Represent proofs and evidence

A theorem, lemma, proposition, or corollary remains a `statement` with warrant `proved`. Its proof is a separate `proof` node, and substantive proof moves are `step` nodes.

Nest a proved statement's proof material inside that statement's canonical node folder as specified by the output layout. Order the steps, link invoked definitions/lemmas with `uses`, link successive logical moves with `entails` when appropriate, and connect the proof or terminal step to the formal statement with `proves`.

Represent experimental observations, cited results, derivations, assumptions, and limitations as ordinary nodes with the appropriate warrant. Claims that interpret those warrants remain separate interpreted statements connected by `supports`, `entails`, `qualifies`, or `challenges` as appropriate.

If a proof appears problematic, record the issue at the proof/step level and relate it with `challenges` or a limitation note. Do not silently relabel the theorem itself to match the digest author's confidence.

## Project-state boundary

Unless the user separately requests broader integration and the project rules authorize it, a paper digest may create or update only the paper package and its containing paper index under the canonical Background directory.

Do not modify as a side effect:

- `task-graph.md`;
- `resolution.md`;
- `roadmap.yaml`;
- `ROADMAP.md`;
- task lifecycle state;
- project history unless local rules explicitly require a history record for background changes; or
- `dictionary.md`.

Preserve source notation inside the digest even when it differs from project notation. Note a genuine notation collision rather than rewriting the source or silently changing the project dictionary.

## Validate before reporting completion

Audit the Markdown package manually and with any repository-native checks that are available:

- every in-scope source unit has exactly one primary coverage assignment;
- unit IDs and node IDs are unique;
- every canonical node has exactly one home;
- echoes point to an existing node rather than creating duplicate ideas;
- every relative Markdown link resolves to an existing file;
- every relation uses an allowed type and valid node IDs;
- every target is answered, explicitly open, or explicitly outside the completed scope;
- interpreted claims have visible support/entailment or an explicit note that the source leaves them unsupported;
- proof steps are ordered and source-anchored;
- coverage counts agree with the section ledgers;
- source provenance and extraction limitations are stated;
- no Python, JSON, or HTML digest artifacts were introduced; and
- the saved files were reread after writing.

For a substantive repository mutation, use the project's required scoped branch and review workflow. Run the strongest applicable project validation and distribution compatibility checks available in the environment.

## Report and stop

Report the canonical digest path, paper/version, coverage counts, number of semantic nodes and relations, inferred-relation count, and any undigested remainder or source-quality limitation. State explicitly that the digest is a source-derived background map, not an independently verified project result.

After producing and validating the requested digest, stop. Do not continue into literature synthesis, task creation, or research conclusions unless the user asks for that next operation.
