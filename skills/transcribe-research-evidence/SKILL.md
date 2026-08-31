---
name: transcribe-research-evidence
description: Faithfully record user-specified or identified content as a Markdown evidence file inside an existing Research-Agent task folder. Use when the user asks to transcribe, preserve, save, or record a proof, note, conversation result, excerpt, or other specified content as task evidence without interpreting it, advancing the task, or changing roadmap/task completion state.
---

# Transcribe Research Evidence

Treat transcription as a preservation action, not a research or completion action.

## Required target

1. Read the target project's current `AGENTS.md`.
2. Resolve and verify the existing canonical task folder from the user-supplied task ID or path. If the material is genuinely project-global background rather than task-specific evidence, use the root task's canonical `Tasks/T001-<root-slug>/Background/` location; do not create or use a separate top-level `Background/` directory.
3. Require the content to record and a destination Markdown filename or relative path. If the user did not provide a filename and project rules do not define one, ask for the filename rather than inventing a canonical evidence name.
4. Do not create a new task merely to satisfy a transcription request.

## Dictionary check

Before writing, consult the current `dictionary.md` for terminology and notation relevant to the supplied content.

- Detect symbols already assigned a different meaning.
- Detect concepts that already have project notation.
- Do not silently resolve a project-level conflict by changing the evidence or dictionary.
- If user authority is required to resolve a real conflict, surface it before writing the conflicting project-authored notation unless the user already supplied a decision.

Distinguish source-faithful transcription from project-authored exposition. Preserve source notation when fidelity requires it; surrounding project-authored material follows project conventions.

## Fidelity

Preserve wording, ordering, equations, code, citations, headings, qualifications, uncertainty, and stated source information. Make only the minimal Markdown changes needed to represent the specified content cleanly.

Do not summarize, improve, correct, normalize, expand, infer, or strengthen the content unless the user explicitly requests that transformation.

## Evidence boundary

As part of transcription alone, do not modify:

- `task-graph.md`;
- `resolution.md`;
- `roadmap.yaml`;
- `ROADMAP.md`;
- task lifecycle status;
- project history; or
- `dictionary.md`.

A later user-directed research turn may interpret the evidence and integrate it into the result graph.

## Write and verify

1. Write only the requested evidence file unless the user explicitly requested additional changes.
2. Verify that the saved file exists at the requested path and substantively matches the supplied content.
3. If project-authored mathematics was written, perform the project's required post-write mathematical review without extending the research beyond the requested scope.
4. Report the saved path and any review finding that requires a user decision, then stop.
