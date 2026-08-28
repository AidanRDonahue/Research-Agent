---
name: synthesize-research-project
description: Synthesize a sufficiently developed Research-Agent project into a coherent higher-level exposition, report plan, or paper structure. Use when the user asks to combine completed tasks, identify the main research story, decide which branches belong in the primary synthesis, separate tangential or follow-up directions, detect missing connective results, or turn task resolutions into a manuscript-level outline or draft. Preserve exact hypotheses and limitations, keep roadmap order distinct from exposition order, and follow the current project AGENTS.md.
---

# Synthesize Research Project

Build a coherent exposition from established project results without rewriting the research history or manufacturing completeness.

## Workflow

1. Ground the synthesis in the target project.
   - Verify the repository and current default branch.
   - Read the current project `AGENTS.md` first.
   - Read `dictionary.md` before normalizing notation or terminology.
   - Read the canonical roadmap and identify the tasks relevant to the requested synthesis scope.
   - Read the relevant completed `resolution.md` files, declared dependencies, and cross-links.
   - Read task-local evidence only when needed to verify a synthesis claim, resolve an ambiguity, or understand a dependency.

2. Define the synthesis boundary.
   - Identify the overarching question or theme being synthesized.
   - Identify which completed, negative, inconclusive, and unresolved tasks are relevant.
   - Do not assume every roadmap branch belongs in the final exposition.

3. Build an evidence-backed result map.
   - Record the major results available for synthesis.
   - Preserve exact hypotheses, conclusions, limitations, and scientific outcomes from their source tasks.
   - Record which results depend on which earlier results.
   - Flag missing lemmas, connective arguments, incompatible assumptions, notation conflicts, or unresolved gaps.

4. Separate research history from exposition structure.
   - Treat the roadmap as the record of how the research developed.
   - Choose exposition order according to logical dependency and explanatory clarity, not task creation order.
   - Do not alter roadmap history merely to make it resemble the eventual manuscript.

5. Classify branches by role.
   - **core**: necessary to answer the synthesis question or support the central results;
   - **supporting**: useful context, examples, validation, or auxiliary results;
   - **negative/inconclusive**: informative failed directions or limitations that may deserve discussion;
   - **follow-up**: valid research branches not needed for the current synthesis;
   - **unresolved prerequisite**: a gap that blocks a defensible synthesis claim.

6. Propose the synthesis before writing a final artifact.
   - Give a concise central narrative.
   - Give an ordered section or theorem dependency outline.
   - Identify which tasks feed each section.
   - Identify branches omitted from the primary narrative and why.
   - Identify unresolved prerequisites or claims that must be weakened.
   - If the user explicitly requested immediate drafting and the evidence is sufficient, proceed directly to the requested artifact after performing this analysis internally.

7. Draft only supported claims.
   - Never strengthen a theorem beyond its task resolution.
   - Preserve assumptions and failure conditions.
   - Integrate notation according to the project dictionary; surface conflicts that require user authority.
   - When multiple task resolutions overlap, reconcile them explicitly rather than duplicating or silently merging incompatible claims.
   - Distinguish established results from interpretation, motivation, conjecture, and future work.

8. Preserve follow-up research value.
   - Keep unused branches visible as possible later papers, projects, or appendices.
   - Do not delete or downgrade a valid branch merely because it does not fit the present exposition.
   - Treat negative and inconclusive results as possible methodological insight, limitation, or future-work context when relevant.

9. Mutate project state only when requested.
   - If the user asks only for an outline or synthesis analysis, do not modify roadmap, task status, or history.
   - If the user asks to save a synthesis artifact, use the project-prescribed location or obtain the necessary destination from existing project conventions.
   - Validate references and any changed project files before publication.

## Default synthesis output

Unless the user requests another format, report:

1. **central story** — the shortest accurate description of what the completed work establishes;
2. **core result chain** — the logical dependency sequence of the main results;
3. **proposed exposition structure** — sections or theorem progression with source tasks;
4. **supporting material** — examples, computation, validation, or contextual results;
5. **gaps and limitations** — unresolved prerequisites, weakened claims, or incompatible assumptions;
6. **follow-up branches** — worthwhile research not required for the present synthesis.

## Boundaries

- Do not mark unresolved tasks complete to make the synthesis cleaner.
- Do not silently strengthen, generalize, or homogenize source-task conclusions.
- Do not treat every completed branch as mandatory manuscript content.
- Do not alter roadmap history to match exposition order.
- Do not claim a complete answer when unresolved prerequisites remain.
- Do not create a final paper or report artifact unless the user requests one.
