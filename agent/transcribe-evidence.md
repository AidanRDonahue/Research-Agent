# Transcribe evidence

## Purpose

Record user-specified content as a Markdown evidence file inside an existing task folder. This is a transcription action, not a research or completion action.

## Required target

The user must identify the task folder or stable task ID and the content to record. Use the existing canonical task folder under `Tasks/<STABLE-ID>-<slug>/`. If the user gives only a stable ID, resolve its current canonical folder from the repository before writing.

Use the filename or relative Markdown path specified by the user. If no filename is supplied, ask the user what filename they want rather than inventing a canonical evidence name.

Do not create a new research node merely to satisfy a transcription request. If the specified task folder does not exist, report that mismatch and stop.

## Dictionary check before transcription

Before rendering or writing the evidence, consult the current `dictionary.md` for project-defined terminology and notation relevant to the supplied content. Check whether any symbol the evidence would introduce is already assigned a meaning, whether the same concept already has recorded notation, and whether the supplied terminology conflicts with an existing project convention.

Do not silently resolve a notation or terminology conflict by changing either the supplied evidence or the dictionary. When the conflict can only be reconciled by a project-level choice, bring it to the user's attention and ask how they want it handled before writing the conflicting notation. If the user has already supplied an explicit instruction that resolves the conflict, follow that instruction and preserve the decision faithfully.

The dictionary check does not authorize rewriting source material merely to normalize notation. Distinguish verbatim or source-faithful transcription from project-authored mathematical exposition: source-faithful material should remain faithful, while any surrounding project-authored notation should follow `dictionary.md` and the repository's mathematical conventions.

## Transcription fidelity

Preserve the specified content faithfully. Preserve wording, ordering, equations, code, citations, headings, lists, qualifications, uncertainty, and stated source information. Make only the minimal Markdown formatting changes required to represent the supplied content cleanly.

Do not summarize, improve, reconcile, correct, normalize, expand, infer, or strengthen the content unless the user explicitly asks for that transformation. Do not silently convert discussion into a stronger research claim.

If the content comes from an attachment or cited source, transcribe only the portion the user identified. Do not fill gaps from general knowledge or unrelated repository context.

## Evidence boundary

Treat the resulting file as task-local evidence because the user directed it to the task folder. Do not infer what conclusion it proves or how much evidentiary weight it carries.

As part of transcription alone, do not modify `task-graph.md`, `resolution.md`, `roadmap.yaml`, `ROADMAP.md`, lifecycle status, project history, or `dictionary.md`. A later user-guided research turn may interpret the evidence or integrate it into a result-dependency graph when the user directs that work.

Do not continue researching the task after the file is written. If the evidence contains project-authored mathematics or presents a proposed new mathematical result, complete the required post-write mathematical review from `agent/validation.md` before reporting the transcription complete. That review is an audit of the written material, not permission to extend the research beyond the user's requested scope.

## Write procedure

1. Resolve and verify the existing target task folder.
2. Consult `dictionary.md` for notation or terminology already assigned to the concepts and symbols in the supplied material; resolve user-authority conflicts before writing.
3. Resolve the user-specified `.md` destination within that task folder.
4. Render the supplied content faithfully in Markdown.
5. Write only the requested evidence file unless the user explicitly requested additional repository changes.
6. Verify that the saved file exists at the requested path and that its substantive content matches the supplied material.
7. When the written evidence includes mathematics, perform the applicable post-write mathematical review required by `agent/validation.md`, including the proposed-result standardness audit when relevant.
8. Report the saved path, any review finding that requires a user decision, and stop at that natural decision point.

If overwriting an existing evidence file, show or describe the existing target and make the replacement only when the user's instruction clearly authorizes it.