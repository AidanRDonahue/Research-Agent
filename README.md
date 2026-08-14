# Research Organization Agent

**This agent is designed for guided research on long, complex questions.** Its primary purpose is to help a user and a language model stay on-track across research that is too large, branching, technical, or evidence-heavy to answer reliably in a single prompt or a single uninterrupted model response.

Long research problems create a predictable failure mode for models: the model may lose the original question, silently change assumptions, skip unresolved dependencies, mix evidence with conjecture, follow an attractive side path, or try to finish the whole problem before the user has had a chance to inspect and redirect the reasoning. This agent provides a persistent project structure and a guided conversational workflow intended to reduce those failures.

Instead of asking the model to solve a large question all at once, the project is organized into bounded research tasks. The user then works through those tasks **with the model, one deliberate step at a time**. The repository preserves the question, dependencies, terminology, evidence, intermediate results, unresolved issues, and task state so each conversation can remain anchored to the actual research program.

The goal is not autonomous research. The goal is **disciplined, user-directed research over many turns**, where the model can do substantial reasoning, calculation, coding, source analysis, or experimentation while the user retains control over what question is being pursued and what happens next.

Copy `AGENTS.md` and the `agent/` directory into the root of a target repository to instantiate this workflow. `AGENTS.md` is the core authority. It defines repository authority, project conventions, roadmap governance, module routing, and the interaction model for research work. Supporting modules cover bootstrap, repository operations, validation, node workflow, context scoping, mathematical research, and faithful evidence transcription.

## Quick start: conversational prompts

You do not need to fill out a large template before using the agent. A normal first-use sequence can be driven by a few short prompts with placeholders for your own project.

### 1. Initialize the project

A concise initialization prompt is:

```text
Use this agent (<RESEARCH-AGENT URL>) to build a project around the question:
"<ROOT RESEARCH QUESTION>"

Instantiate the project in <OWNER>/<REPOSITORY>, using <SUPPLIED PAPER / NOTES / SOURCES> as background. Follow all mandates in the agent documents and copy the agent into the project.
```

If there is no initial background source, omit that clause. The important pieces are the governing agent, target repository, and root research question. Additional scope, terminology, and validation constraints can be supplied when they are already known.

### 2. Ask for a useful first branch

Once `T001` has been created, a user can simply ask:

```text
What is a good starting point for branching from this task?
```

or more explicitly:

```text
Given T001, what would be a useful first bounded research direction?
```

The model may suggest a branch, but the suggestion is not yet a task.

### 3. Define the task through conversation

If a suggested direction looks useful, continue with:

```text
Yes, let's do that by starting a conversation. Ask me questions.
```

The task-intake workflow should then narrow the idea one item at a time. The user can answer naturally rather than writing a formal task contract. Useful answers often sound like:

```text
Let's focus on <SPECIFIC OBJECT / CASE / METHOD>.
```

```text
Start with <BASELINE OR SPECIAL CASE>, then generalize.
```

```text
Keep this task limited to <IN-SCOPE DIRECTION> and leave <OUT-OF-SCOPE DIRECTION> for later.
```

```text
I want a proof whenever we claim that <CLASSIFICATION / CORRESPONDENCE / EXTENSION> is correct.
```

The agent is responsible for turning those ordinary research decisions into the required task metadata, scope, method, stopping rules, outcome branches, assumptions, validation, and evidence graph.

### 4. Publish the task when the scope is settled

When the conversation has reached a precise bounded target, the user can say:

```text
Sounds good. Read AGENTS.md and create a new task investigating that setting.
```

The agent should then follow the repository's node-creation workflow, create the canonical task folder, keep the resolution pending, synchronize the roadmap, validate the change, and publish it through the repository workflow.

See [`Getting-Started.md`](Getting-Started.md) for a complete example of this conversational narrowing process using a deliberately generic mathematical question.

## Why use this agent?

Use this agent when the research question is large enough that maintaining continuity and discipline across many model turns matters as much as producing any one answer.

It is especially useful when:

- the main question must be decomposed into dependent subquestions;
- reasoning will unfold across many conversations or sessions;
- assumptions, definitions, notation, or conventions must remain stable;
- multiple evidence files, calculations, experiments, or sources need to be connected without losing provenance;
- a model is likely to drift into adjacent questions or prematurely synthesize an answer;
- negative, partial, or inconclusive results need to remain visible rather than being smoothed over;
- the user wants to inspect and redirect the research process at meaningful decision points; or
- the eventual answer must be reconstructible from an explicit chain of evidence rather than from model memory alone.

The repository acts as persistent research memory, while the task workflow acts as a **scope-control mechanism for the model**. Each task tells the model what problem is currently admissible, which prior results may be used, what evidence belongs to the task, and what remains unresolved. The user decides which part of that bounded problem to work on next.

## Intended workflow: guided research, not autonomous completion

Creating a task establishes a bounded research contract: the question, parent, dependencies, method, stopping rules, expected evidence, and possible outcomes. **It does not tell the model to go away and finish the task autonomously.** A task is a container for a continuing research conversation.

Working on a task should be a guided conversation between the user and their model. The user chooses the current question, proposed argument, experiment, calculation, source, or direction. The model works deeply on that bounded step, explains what was established and what remains open, and then stops at a natural decision point so the user can inspect the result and decide what to do next.

This interaction pattern is central to the agent. For a difficult question, the expected sequence is not:

```text
User gives task -> model attempts entire task -> model produces final answer
```

Instead, the expected sequence is closer to:

```text
User and model define a bounded task
        ↓
User chooses the next question or research step
        ↓
Model works on that step using the permitted context
        ↓
Result or evidence is inspected and, when useful, preserved
        ↓
Model states what is established and what remains open
        ↓
User chooses the next direction
        ↓
...repeat as needed...
        ↓
User explicitly requests task completion when the evidence is ready
```

The model may suggest useful next steps, but it should not silently execute them. It should not treat a task's method, dependency graph, or apparent next proof step as permission to run ahead. If the evidence appears sufficient to complete a task, the model should say so and wait for the user to explicitly request the completion workflow.

This is how the agent is intended to keep models on-track while answering long, complex questions: **scope is made explicit, evidence is persisted, unresolved questions remain visible, and the user repeatedly re-authorizes the next research step.**

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

Prepare as much of the following as is known. Leave unknown items explicitly undecided rather than guessing. The concise initialization prompt above is enough to get started when most of these details are not known yet.

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

For most new projects, the concise prompt from the quick-start section is enough:

```text
Use this agent (<RESEARCH-AGENT URL>) to build a project around the question:
"<ROOT RESEARCH QUESTION>"

Instantiate the project in <OWNER>/<REPOSITORY>, using <BACKGROUND MATERIAL> as background. Follow all mandates in the agent documents and copy the agent into the project.
```

If you want to specify the project structure and constraints in more detail up front, use the expanded form below:

```text
Initialize this repository as a guided research project using AGENTS.md.

This project will be used to work through a long or complex research question over multiple user-directed conversations. Preserve the project state so the model can remain anchored to the current question, dependencies, evidence, and unresolved issues rather than attempting to solve the whole research program at once.

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

For an empty repository, the minimum useful inputs are repository identity, a root research question or objective, and enough context to describe the project purpose. Scope and other details can remain undecided until the guided conversation makes them necessary.

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

A natural way to define the first child of `T001` is conversational rather than form-driven:

```text
What is a good starting point for branching from this task?
```

After choosing a promising direction:

```text
Yes, let's do that by starting a conversation. Ask me questions.
```

Answer the intake questions normally until the target, scope, assumptions, proof/evidence standard, and stopping point are clear. Then publish the result with:

```text
Sounds good. Read AGENTS.md and create a new task investigating that setting.
```

You can also initiate intake directly with a more explicit prompt:

```text
Define a new research task for this project. The broad goal is:
<DESCRIBE THE RESEARCH QUESTION OR ACTION>

Use the current roadmap, dictionary, dependencies, and existing evidence as authority. Follow the task-intake workflow in AGENTS.md and the routed node instructions. Do not publish the task until the required intake information is complete.
```

The task-intake conversation establishes the action-oriented title, parent, relation to parent, uncertainty reduced, dependencies, bounded method, stopping rules, outcome branches, exclusions, assumptions, conventions, validation, and planned result-dependency graph. The user does not need to supply all of those fields directly; the agent should derive them from the guided conversation without inventing research decisions the user has not made.

## Start or continue work on an existing task

This is the normal research workflow and the main way the agent should be used. Use a prompt like:

```text
Work with me on research task <STABLE-ID> as a guided conversation.

For this turn, I want to focus on:
<CURRENT QUESTION, ARGUMENT, CALCULATION, EXPERIMENT, SOURCE, OR DECISION>

Address this bounded step using the task's permitted context. Explain what we establish, what remains uncertain, and the most relevant next options. Do not continue into later task steps or try to finish the task unless I explicitly direct you to do so.
```

You do not need to restate the whole task each turn. The repository exists precisely so a long research effort can maintain continuity without forcing the user to reprompt the entire problem. Once the task is established, subsequent prompts can simply continue the discussion, for example:

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

For especially long or difficult tasks, regularly preserve important intermediate results as task evidence. This gives later conversations a concrete record to work from and reduces dependence on the model remembering an extended discussion correctly.

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

1. Copy `AGENTS.md` and `agent/` into the target repository, or direct the model to copy them as part of initialization when it has repository access.
2. Give the model the target repository and root research question, plus any background sources already available.
3. Run the concise initialization prompt or the expanded form when you need tighter control over project metadata.
4. Review the generated project `README.md`, `dictionary.md`, roadmap, templates, and validation checklist.
5. Add additional shared sources to `Background/` as needed.
6. Ask for a good first branch from `T001`, then tell the agent to start a conversation and ask questions.
7. Answer the task-intake questions naturally until the bounded target and research standard are clear, then explicitly ask the agent to create the task.
8. Work on that task conversationally, one user-directed question or bounded block at a time.
9. Preserve important intermediate results and source material as task-local evidence so later turns remain anchored to the research record.
10. When the task appears ready, explicitly request the completion workflow and validate before merging structural or task-completion changes.
