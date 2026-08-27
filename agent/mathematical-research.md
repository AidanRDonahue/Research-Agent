# Mathematical research

## Research rigor

Classify claims when useful as established fact, cited result, derivation, experimental evidence, numerical evidence, heuristic, or conjecture. Scrutinize assumptions, dimensions, domains/codomains, quantifiers, regularity, compatibility conditions, singular cases, sign conventions, indexing, normalization, and other domain-specific hypotheses. Finite enumeration is evidence only unless it exactly exhausts the explicit finite certificate being claimed.

When a statement fails, identify the exact failure and make only the strongest repair justified by evidence. Keep exact conclusions, statistical conclusions, ordering relations, structural equivalence, experimental evidence, and numerical evidence distinct.

## Guided mathematical work

Mathematical work on an existing node is conversational and user-directed. Address the specific derivation, proof step, example, counterexample, computation, conjecture, or question raised in the current turn. Do not continue through an entire proof strategy or research program merely because a next step is available.

If progressing requires introducing a concept, framework, reformulation, or equivalent problem that has not previously been part of the discussion, first explain why that move appears necessary or materially useful. This includes translating the problem into a different area of mathematics, invoking an unfamiliar equivalent formulation, or changing the mathematical viewpoint in a way that opens a substantially different line of attack. Treat that as a decision point: present the justification and ask whether the user wants to explore that alternate train of thought before pursuing it, unless the user has already explicitly authorized that broader direction.

After a substantive mathematical result, state what was established, note unresolved assumptions or branches, and present the most relevant next options. Wait for the user's direction before pursuing another branch unless the user explicitly requested a larger bounded block of work.

Do not turn partial progress into a completed theorem, task resolution, or final claim without the explicit completion workflow.

## Mathematical Markdown conventions

When mathematical Markdown is used, prefer GitHub's backtick-delimited inline form ``$`...`$``. For display math, prefer fenced `math` blocks when dollar-delimited display math is unreliable. Do not use `\tag{...}` inside fenced `math` blocks. For numbered display equations, put the equation number in ordinary Markdown immediately outside the fenced block and keep references such as `(1)` in prose.

For named mathematical operations or operators that require upright Roman typesetting, use `\mathrm{...}` rather than `\operatorname{...}` unless `dictionary.md` explicitly records another project-specific convention. Preserve TeX backslashes exactly and follow any additional mathematical conventions recorded in `dictionary.md` or other designated project authorities.
