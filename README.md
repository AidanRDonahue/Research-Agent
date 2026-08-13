# Research Organization Agent

This repository contains a reusable instruction system for creating and maintaining structured research projects. Copy `AGENTS.md` and the `agent/` directory into the root of a target repository, then use those instructions to initialize and operate the project.

`AGENTS.md` is the core authority. It defines repository authority, project conventions, roadmap governance, module routing, and the interaction model for research work. Supporting modules cover bootstrap, repository operations, validation, node workflow, context scoping, mathematical research, and faithful evidence transcription.

## Intended workflow

The agent is designed to organize research without replacing the user's role in directing it.

Creating a task establishes a bounded research contract: the question, parent, dependencies, method, stopping rules, expected evidence, and possible outcomes. **It does not tell the model to go away and finish the task autonomously.**

Working on a task should be a guided conversation between the user and their model. The user chooses the current question, proposed argument, experiment, calculation, source, or direction. The model works on that bounded step, explains what was established and what remains open, and then stops at a natural decision point so the user can choose what to do next.

The model may suggest useful next steps, but it should not silently execute them. If the evidence appears sufficient to complete a task, the model should say so and ask whether the user wants to enter the completion workflow. A task should only be completed when the user explicitly asks to evaluate, resolve, or complete it.

## What this agent manages

An instantiated project uses the canonical structure defined in `agent/bootstrap.md`:

- `README.md` for project orientation
- `AGENTS.md` and `agent/` for operating instructions
- `dictionary.md` for canonical terminology and notation
- `roadmap.yaml` for canonical project state
- `ROADMAP.md` for the human-readable Mermaid roadmap
- `Tasks/` for one canonical folder per research node
- `Background/` for shared foundations used by multiple tasks
- `templates/` for task templates
- `history/roadmap-events.jsonl` for append-only project-state history
- `checks/project-system-checklist.md` for project-system validation

Task-specific evidence belongs in the corresponding `Tasks/<STABLE-ID>-<slug>/` folder unless it genuinely functions as shared project background.

## Information to provide before initialization

Prepare as much of the following as is known. Leave unknown items explicitly undecided rather than guessing.

### Project identity

Provide the repository owner or organization, repository name, project title, concise purpose statement, project scope, and exclusions.

### Project orientation

Describe the research problem or program, intended outputs, expected artifact types, and the working procedure contributors should follow.

### Terminology and conventions

Provide domain-specific terminology, definitions, notation, naming rules, units, sign conventions, indexing conventions, normalization rules, and other conventions that must remain stable. These become the basis of `dictionary.md`.

### Initial research state

If known, provide the root objective, major existing questions, dependencies, cross-links, completed work, and artifacts that should count as evidence. Roadmap metadata alone should not be treated as evidence.

### Background material

Identify specifications, publications, prior work, accepted assumptions, reference material, design documents, or other sources that should serve as shared foundations across multiple tasks.

### Repository-specific constraints

Provide required CI commands, tests, linting or formatting commands, branch-protection rules, generated files, preserved directories, validators, or structural requirements.

## Instantiate a new project

First copy these files to the root of the target repository:

```text
AGENTS.md
agent/
├── bootstrap.md
├── repository-operations.md
├── validation.md
├── node-workflow.md
├── context-scoping.md
├── mathematical-research.md
└── transcribe-evidence.md
```

Then use a prompt like:

```text
Initialize this repository as a research project using AGENTS.md.

Repository: <OWNER>/<REPOSITORY>
Project title: <PROJECT TITLE>
Purpose: <PURPOSE>
Scope: <IN-SCOPE WORK>
Out of scope: <EXCLUSIONS>
Primary artifact types: <CODE / PAPERS / DATA / MODELS / EXPERIMENTS / DESIGNS / OTHER>

Project terminology and conventions:
<TERMS, DEFINITIONS, NOTATION, NAMING RULES, UNITS, OR "NONE YET">

Initial research state:
<ROOT OBJECTIVE, KNOWN TASKS, DEPENDENCIES, EXISTING RESULTS, OR "START WITH ONLY A ROOT OBJECTIVE">

Repository-specific validation:
<TESTS, CI, LINTING, STRUCTURAL CHECKS, OR "NO ADDITIONAL VALIDATION YET">

Preserve existing project-specific artifacts that do not conflict with the canonical project system. Do not invent missing research results. Create the required project structure, validate it, and report unresolved decisions or missing inputs.
```

For an empty repository, the minimum useful inputs are repository identity, project title, purpose, scope, and a root objective.

## Upload shared background information

```text
Add the supplied files and sources as background material for this project.

Inspect each source and preserve its provenance. Put genuinely reusable project-wide material under Background/. Do not treat unsupported claims as established project results. Update dictionary.md only for terminology or conventions supported by the material or explicitly supplied by me. Do not create roadmap tasks merely because a source contains open questions.

After organizing the material, report what was added, where it was placed, what became accepted project-wide context, and what remains source material only.
```

## Upload evidence for one task

Use this when you are supplying an existing file or source artifact that should be organized as task evidence:

```text
Add the supplied material as evidence for task <STABLE-ID>.

Keep it in the canonical Tasks/<STABLE-ID>-<slug>/ folder using an appropriate evidence subdirectory such as notes/, data/, experiments/, scripts/, or references/. Treat it as task-specific unless there is a clear reason it is a shared foundation.

Update the task result-dependency graph only for actual evidence or established results. Do not mark the task completed unless I explicitly ask for completion.
```

## Transcribe specified content as task evidence

Use the `transcribe-evidence.md` workflow when the useful evidence already exists in the conversation, an attachment, or another identified source and you want the model to **record it faithfully without interpreting it or advancing the task**.

Specify the task and the Markdown destination. For example:

```text
Transcribe the following content as evidence for task <STABLE-ID>.

Save it as:
Tasks/<STABLE-ID>-<slug>/notes/<FILENAME>.md

Content to record:
<SPECIFIED CONTENT, OR IDENTIFIED CONTENT FROM THE CURRENT CONVERSATION / ATTACHMENT>

Preserve the content faithfully in Markdown. Do not summarize, improve, correct, analyze, or strengthen it. Do not update task-graph.md, resolution.md, the roadmap, task status, history, or dictionary.md. After saving the evidence file, report its path and stop.
```

If you identify the task by stable ID but do not know its current folder slug, the model may resolve the canonical folder from the repository. If you do not supply a filename, the transcription workflow should ask you for one rather than inventing a canonical evidence filename.

This workflow is useful for preserving a result reached during a guided conversation before deciding what it means for the task. Recording the content and interpreting its evidentiary consequence are intentionally separate actions.

## Define a new research task

```text
Define a new research task for this project. The broad goal is:
<DESCRIBE THE RESEARCH QUESTION OR ACTION>

Use the current roadmap, dictionary, dependencies, and existing evidence as authority. Follow the task-intake workflow in AGENTS.md and the routed node instructions. Do not publish the task until the required intake information is complete.
```

The task-intake conversation establishes the action-oriented title, parent, relation to parent, uncertainty reduced, dependencies, bounded method, stopping rules, outcome branches, exclusions, assumptions, conventions, validation, and planned result-dependency graph.

## Start or continue work on an existing task

This is the normal research workflow. Use a prompt like:

```text
Work with me on research task <STABLE-ID> as a guided conversation.

For this turn, I want to focus on:
<CURRENT QUESTION, ARGUMENT, CALCULATION, EXPERIMENT, SOURCE, OR DECISION>

Address this bounded step using the task's permitted context. Explain what we establish, what remains uncertain, and the most relevant next options. Do not continue into later task steps or try to finish the task unless I explicitly direct you to do so.
```

You do not need to restate the whole task each turn. Once the task is established, subsequent prompts can simply continue the discussion, for example:

```text
Let's test the second assumption first. What fails if <ASSUMPTION> is removed?
```

or:

```text
Before we prove that lemma, compare these two possible approaches and tell me what each would require.
```

or:

```text
Use the attached paper only to check whether it supports the claim we just made. Don't advance the rest of the task yet.
```

The model should treat each of these as a bounded conversational step, not permission to execute the rest of the task method.

## Import existing research work

```text
Reconcile the supplied existing research work with this repository's project system.

For each item, determine whether it belongs in Background/, an existing task folder, a new task folder, or as a project-specific artifact outside the governance directories. Preserve evidence boundaries and do not infer completion from filenames or summaries alone.

Identify any historical state that cannot be reconstructed reliably from the available evidence.
```

## Change project structure

```text
Modify the project structure to support this need:
<DESCRIBE THE NEW DIRECTORY, ARTIFACT TYPE, OR WORKFLOW>

Reason:
<WHY THE CURRENT STRUCTURE IS INSUFFICIENT>

Constraints:
<FILES OR DIRECTORIES THAT MUST REMAIN UNCHANGED, MIGRATION REQUIREMENTS, OR OTHER LIMITS>

Preserve the canonical project-system responsibilities. If the requested structure would create a competing canonical location or violate an invariant, explain the conflict and make the smallest compatible alternative change. Validate the resulting structure before publishing it.
```

## Change roadmap structure

```text
Change the roadmap structure as follows:
<DESCRIBE THE MOVE, PARENT CHANGE, DEPENDENCY CHANGE, CROSS-LINK, OR REORGANIZATION>

Do not create a new research node unless required. Preserve stable IDs, verify parent and dependency acyclicity, update display indices when applicable, synchronize roadmap.yaml and ROADMAP.md, preserve direct Mermaid-node links to task folders, and validate the result.
```

## Complete a task

Completion is an explicit workflow, separate from ordinary task conversation. Use:

```text
Evaluate task <STABLE-ID> for completion and complete it if the repository evidence supports doing so.

Do not rewrite the original question to fit the result. Verify the declared premises and dependencies, produce the required self-contained resolution at the supported scope, update the evidence graph, record outcome separately from lifecycle status, synchronize roadmap.yaml and ROADMAP.md, append required history, and validate the project.
```

Negative and inconclusive outcomes should be recorded accurately rather than converted into artificial success outcomes.

## Validate a project

```text
Validate this repository against AGENTS.md and the routed validation instructions.

Check the canonical structure, roadmap/task consistency, stable IDs, parent and dependency validity, task folders, required task files, pending versus completed resolutions, evidence graphs, templates, history, terminology conventions, and checks/project-system-checklist.md. Also run any repository-specific validators that are available.

Report failures and validation limitations explicitly.
```

## Recommended first-use sequence

1. Copy `AGENTS.md` and `agent/` into the target repository.
2. Supply project identity, purpose, scope, terminology, initial state, and repository-specific constraints.
3. Run the initialization prompt.
4. Review the generated project `README.md`, `dictionary.md`, roadmap, templates, and validation checklist.
5. Add shared sources to `Background/`.
6. Define the first bounded task through the intake conversation.
7. Work on that task conversationally, one user-directed question or bounded block at a time.
8. Use the transcription workflow when you want to preserve specified conversational or source content as task-local Markdown evidence without interpreting it yet.
9. When the task appears ready, explicitly request the completion workflow.
10. Validate before merging structural or task-completion changes.
