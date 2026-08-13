# Transcribe evidence

## Purpose

Record user-specified content as a Markdown evidence file inside an existing task folder. This is a transcription action, not a research or completion action.

## Required target

The user must identify the task folder or stable task ID and the content to record. Use the existing canonical task folder under `Tasks/<STABLE-ID>-<slug>/`. If the user gives only a stable ID, resolve its current canonical folder from the repository before writing.

Use the filename or relative Markdown path specified by the user. If no filename is supplied, ask the user what filename they want rather than inventing a canonical evidence name.

Do not create a new research node merely to satisfy a transcription request. If the specified task folder does not exist, report that mismatch and stop.

## Transcription fidelity

Preserve the specified content faithfully. Preserve wording, ordering, equations, code, citations, headings, lists, qualifications, uncertainty, and stated source information. Make only the minimal Markdown formatting changes required to represent the supplied content cleanly.

Do not summarize, improve, reconcile, correct, normalize, expand, infer, or strengthen the content unless the user explicitly asks for that transformation. Do not silently convert discussion into a stronger research claim.

If the content comes from an attachment or cited source, transcribe only the portion the user identified. Do not fill gaps from general knowledge or unrelated repository context.

## Evidence boundary

Treat the resulting file as task-local evidence because the user directed it to the task folder. Do not infer what conclusion it proves or how much evidentiary weight it carries.

As part of transcription alone, do not modify `task-graph.md`, `resolution.md`, `roadmap.yaml`, `ROADMAP.md`, lifecycle status, project history, or `dictionary.md`. A later user-guided research turn may interpret the evidence or integrate it into a result-dependency graph when the user directs that work.

Do not continue researching the task after the file is written.

## Write procedure

1. Resolve and verify the existing target task folder.
2. Resolve the user-specified `.md` destination within that task folder.
3. Render the supplied content faithfully in Markdown.
4. Write only the requested evidence file unless the user explicitly requested additional repository changes.
5. Verify that the saved file exists at the requested path and that its substantive content matches the supplied material.
6. Report the saved path and stop at that natural decision point.

If overwriting an existing evidence file, show or describe the existing target and make the replacement only when the user's instruction clearly authorizes it.