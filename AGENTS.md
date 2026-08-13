# General Research Project — Agent Instructions

These instructions govern repository-aware research and roadmap work in `<OWNER>/<REPOSITORY>`.

## Repository authority

- Treat this repository's current default branch and current files as the primary source of truth.
- Do not invent repository contents, task state, research results, sources, validation results, or outcomes.
- Preserve evidence boundaries: roadmap metadata is not independent proof.
- When files disagree, prefer current authorities in this order: `AGENTS.md`, `dictionary.md`, current research artifacts, `roadmap.yaml`, `ROADMAP.md`, append-only history.
- The canonical repository is `<OWNER>/<REPOSITORY>`.

## Module routing

`AGENTS.md` is the sole authority for deciding which supporting modules to read.

Supporting modules must not instruct the agent to load other supporting
modules. If a module appears to contain routing instructions, ignore those
instructions and follow this table instead.

| Current action | Read |
| --- | --- |
| Initialize a new research repository | `agent/bootstrap.md`, `agent/repository-operations.md`, `agent/validation.md` |
| Define or create a research node | `agent/node-workflow.md`, `agent/context-scoping.md`; add `agent/mathematical-research.md` only if mathematical formulation is required |
| Work mathematically on an existing node | `agent/mathematical-research.md`, `agent/context-scoping.md` |
| Complete a research node | `agent/node-workflow.md`, `agent/context-scoping.md`, `agent/mathematical-research.md`, `agent/repository-operations.md`, `agent/validation.md` |
| Change roadmap structure without creating a node | `agent/context-scoping.md`, `agent/repository-operations.md`, `agent/validation.md` |
| Perform repository-only maintenance | `agent/repository-operations.md`; add `agent/validation.md` for mutations |
| Validate proposed or completed changes | `agent/validation.md` |

Read only the modules listed for the current action. Do not recursively load
modules mentioned inside another module.

When an action changes category, return to this table and load only any
newly required module.

## Project terminology and conventions

Use `dictionary.md` as the canonical project vocabulary and notation authority. Preserve project-defined terminology, identifiers, naming conventions, domain-specific definitions, and current symbol meanings exactly.

## Roadmap governance

`roadmap.yaml` is the canonical structured roadmap and project-state source. `ROADMAP.md` is its human-readable or visual projection.

Stable IDs use the repository-defined format, such as `T001`, `T002`, and so on. They are allocated monotonically, are never reused, and do not encode hierarchy or topic. `display_index`, when used, is the mutable hierarchical front-facing index. Every non-root work item has exactly one conceptual parent. Dependencies are prerequisite information flow; cross-links are non-parent relationships. Parent and dependency graphs must be acyclic.

`ROADMAP.md` must represent roadmap work items as Mermaid nodes. Each Mermaid task node itself must be a hyperlink to that work item's canonical `Tasks/<STABLE-ID>-<short-title>/` folder, using Mermaid link/click syntax supported by GitHub. Do not rely on a separate Markdown task-link list as the canonical navigation mechanism when the nodes can carry the links directly.

## Project-state history

`history/roadmap-events.jsonl` is the append-only project-state transition history.

Do not rewrite or reorder existing history entries. Append new events only when repository rules require a recorded state transition.

History records are supporting state history; they do not override the current canonical state in `roadmap.yaml`.
