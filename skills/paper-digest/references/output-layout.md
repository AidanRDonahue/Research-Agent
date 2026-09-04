# Paper Digest Output Layout

Create one canonical digest package per paper under the project's canonical global Background directory.

Under the current Research-Agent project baseline:

```text
Tasks/T001-<root-slug>/Background/
`-- papers/
    |-- README.md
    `-- <paper-key>/
        |-- README.md
        |-- metadata.md
        |-- relations.md
        |-- storyline/
        |   |-- README.md
        |   `-- Q0001-<root-target>/
        |       |-- README.md
        |       |-- Q0002-<refinement>/
        |       |   `-- README.md
        |       `-- Q0003-<refinement>/
        |           `-- README.md
        |-- nodes/
        |   |-- N0001-<slug>.md
        |   |-- N0002-<slug>.md
        |   `-- N0003-<formal-result>/
        |       |-- README.md
        |       `-- proof/
        |           |-- README.md
        |           |-- S0001-<step>.md
        |           `-- S0002-<step>.md
        `-- coverage/
            |-- README.md
            |-- 01-<section>.md
            `-- 02-<section>.md
```

If the target project's current `AGENTS.md` declares a different canonical Background location or naming convention, follow the project rule and preserve the same internal paper-package semantics unless that also conflicts.

## Paper key

Use a stable filesystem-safe key derived from a durable identifier when possible:

- `arxiv-2401.01234`
- `doi-10.1234-abc.def`
- otherwise `<first-author>-<year>-<short-title>`

Do not create a second key for a revised version of the same canonical paper. Record the digested version/date in `metadata.md` and update the existing package.

## `papers/README.md`

Maintain a compact index of digested papers. Each entry should include:

- paper key and relative link;
- title;
- authors;
- year/version;
- stable identifier/source;
- digestion status (`complete-main-body`, `partial`, or project-specific equivalent); and
- one-line scope note.

Do not turn the index into a literature synthesis.

## Paper `README.md`

Use this as the human entrypoint. Include:

- citation/identity summary;
- digestion scope and source quality;
- the paper's root research question/target in concise terms;
- a short map of the top-level target refinements;
- links to `storyline/`, `relations.md`, `nodes/`, and `coverage/`;
- coverage/node/relation counts; and
- an explicit notice that this is a source-derived background map, not an independently verified project result.

## `metadata.md`

Record source provenance, not semantic conclusions:

```markdown
# Metadata

- Title:
- Authors:
- Year:
- Venue:
- DOI:
- arXiv:
- Digested version/date:
- Source used:
- Source type: LaTeX | HTML | PDF | Markdown | other
- Accessed:
- Digest path:
- Extraction limitations:
- Scope included:
- Scope not fully digested:
```

## Canonical node files

Use `nodes/N####-<slug>.md` for ordinary nodes. Use a directory `nodes/N####-<slug>/README.md` when the node owns nested material such as a proof.

Template:

```markdown
# N0007 — <concise semantic label>

- Kind: statement
- Warrant/subtype: interpreted
- Story function: theory_answer
- Home: u0142
- Source anchors: §3.2, p. 8
- Echoes: u0018, u0061

## Source-faithful paraphrase
<one idea only>

## Relations
- Incoming: [R0012](../relations.md#r0012) — supports from N0006
- Outgoing: [R0019](../relations.md#r0019) — develops N0011

## Notes
- <scope, extraction uncertainty, or distinction from nearby ideas>
```

For constructs and targets replace `Warrant/subtype` with the applicable subtype value.

## Formal result folder

A formal result uses a node directory:

```text
nodes/N0042-main-convergence-theorem/
|-- README.md
`-- proof/
    |-- README.md
    |-- S0001-establish-invariant.md
    `-- S0002-apply-lemma-3.md
```

The formal-result `README.md` is the canonical `statement/proved` node. The `proof/README.md` is the canonical `proof` node. Step files are canonical `step` nodes and may include `Step role: setup|computation|invoke|case-split|conclude`.

Proof step IDs are local to the proof folder (`S0001`, `S0002`, ...). Canonical cross-paper relations should still refer to the parent node plus proof-step relative path when needed.

## `relations.md`

Keep all cross-node relations in one readable ledger so backlinks can be audited without JSON.

```markdown
# Relations

## R0001
- Type: refines
- From: [N0001](nodes/N0001-root-question.md)
- To: [N0002](nodes/N0002-design-goal.md)
- Basis: explicit
- Evidence: u0041 — §1.2
- Note: <optional>

## R0002
- Type: supports
- From: [N0018](nodes/N0018-observation.md)
- To: [N0021](nodes/N0021-interpretation.md)
- Basis: inferred
- Evidence: u0322-u0324 — Fig. 5 discussion
- Note: reconstruction by digest author; source does not name this relation.
```

Use stable `R####` IDs. Preserve IDs across updates when the relation's meaning remains the same.

## `storyline/`

The storyline is a projection, not a second semantic store.

- `storyline/README.md` links to the root target folder and can include a Mermaid navigation diagram if useful.
- Mirror only target-to-target `refines` relations as nested directories.
- Give each target folder a stable storyline ID (`Q0001`, `Q0002`, ...), a slug, and `README.md`.
- The folder README links to the canonical target node and lists `answered_by` links, motivating nodes, and child refinements.
- Do not copy claim prose into the storyline beyond a short navigation label.

Example target README:

```markdown
# Q0002 — Make the construction tractable

- Canonical target: [N0008](../../nodes/N0008-tractability-goal.md)
- Parent target: [Q0001](../README.md)
- Answered by: [N0014](../../nodes/N0014-reparameterized-objective.md)
- Motivated by: [N0006](../../nodes/N0006-original-objective-is-intractable.md)

## Child refinements
- [Q0004 — Preserve endpoint law](Q0004-preserve-endpoint-law/README.md)
```

## `coverage/`

Create `coverage/README.md` plus one ledger per paper section or other manageable contiguous source range.

The summary must include:

- total source units identified;
- `dissected_through` unit;
- count by primary assignment (`home`, `echo`, `edge-evidence`, `discard`, `structure`);
- count of nodes, relations, and inferred relations;
- list of undigested sections/proofs/appendices; and
- extraction limitations.

Section ledger template:

```markdown
# §3 Method — Coverage

| Unit | Anchor | Assignment | Target | Note |
| --- | --- | --- | --- | --- |
| u0121 | §3 ¶1 s1 | home | N0010 | definition |
| u0122 | §3 ¶1 s2 | edge-evidence | R0008 | explicit motivation |
| u0123 | §3 ¶2 s1 | echo | N0004 | repeats intro criterion |
| u0124 | §3 ¶2 s2 | discard | signpost | section roadmap |
```

Use compact source descriptions or very short snippets only when needed to distinguish units; do not reproduce the paper wholesale.

## Relative links

Prefer relative Markdown links within a paper package. The package should remain navigable if its project repository is cloned locally or moved to another branch.
