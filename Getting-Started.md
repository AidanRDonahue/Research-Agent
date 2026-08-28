# Getting Started

This guide shows the shortest path from a versioned Research-Agent release to the creation of a first child research task. For a fully self-contained installation, pinning, upgrade, development, and troubleshooting guide, see [`USING_IN_YOUR_PROJECT.md`](USING_IN_YOUR_PROJECT.md).

## 1. Choose one Research-Agent release

Use a tagged release for repeatable research rather than mixing files from different points on `main`.

From that same release:

- use `RESEARCH_AGENT.md` as the persistent collaborator instructions;
- download `research-agent-skills-v<VERSION>.zip`;
- extract the bundle and install each desired inner `skill.zip`; and
- retain `research-agent-distribution.json` so the exact source commit is observable.

The outer release bundle is not itself a Skill.

## 2. Connect GitHub

Connect the GitHub integration in ChatGPT and configure repository access for the project you want the Research Agent to read or edit. Access to one account or organization does not automatically imply access to every repository.

## 3. Configure the Research Agent

Use `RESEARCH_AGENT.md` from the chosen release tag as the persistent instruction set for the research collaborator. The Agent contains general research behavior only; it does not contain the state or exact rules of a particular research project.

## 4. Install the core Skills

For the complete workflow, install the independently packaged Skills extracted from the release bundle:

- `bootstrap-research-project`
- `define-research-task`
- `transcribe-research-evidence`
- `review-mathematical-result`
- `restructure-research-roadmap`
- `complete-research-task`
- `validate-research-project`
- `synthesize-research-project`

Each package contains generated distribution metadata. Source changes in GitHub do not automatically replace an installed Skill.

## 5. Bootstrap a project

A concise initialization request is:

```text
Initialize <OWNER>/<REPOSITORY> as a Research-Agent project around the question:
"<ROOT RESEARCH QUESTION>"

Use <SUPPLIED PAPER / NOTES / SOURCES> as background.
```

For example:

```text
Initialize <OWNER>/<REPOSITORY> as a Research-Agent project around the question:
"What are the different groups of order n up to isomorphism?"
```

The bootstrap Skill creates the project-local `AGENTS.md`, dictionary, roadmap, task templates, validation checklist, root task `T001`, and—when concrete package metadata is available—`research-agent.lock.json` pinning the external toolchain.

The root task represents the overarching research question. It does not need to be marked resolved before child tasks are created.

## 6. Understand what is persistent

After bootstrap, the target repository rather than model memory stores research state. The important authorities are:

- `AGENTS.md` for local project rules;
- `dictionary.md` for terminology and notation;
- `roadmap.yaml` for canonical roadmap state;
- `ROADMAP.md` for the visual roadmap;
- `Tasks/` for task contracts, evidence, and resolutions; and
- `Background/` for shared foundations.

`research-agent.lock.json` is different: it records external toolchain compatibility and does not override the research authorities above.

## 7. Choose a first branch

The user can ask:

```text
What is a good starting point for branching from T001?
```

The Agent may suggest options, but suggestions are not automatically tasks.

For the example root question about groups of order `n`, useful possibilities might include prime order, prime-square order, order `pq`, finite abelian groups, or a computational census for small `n`.

## 8. Start the task-definition conversation

Once a direction looks useful, say:

```text
Let's create a task for that direction. Start the task-definition conversation.
```

The `define-research-task` Skill asks for the concrete bounded target and gathers the parent relation, dependencies, objective, method, stopping rules, outcome branches, assumptions, validation, and planned result graph without solving the task during intake.

For example:

> **Agent:** Should this be a direct child of T001, studying one manageable family of values of `n`?
>
> **User:** Yes.
>
> **Agent:** Should the setting be `|G| = pq` for distinct primes `p < q`?
>
> **User:** Yes.
>
> **Agent:** Do you want examples, or a proof that the classification is complete?
>
> **User:** I want the complete classification with a proof.

## 9. Publish the task

When the scope is settled, say:

```text
Create the task with that scope.
```

The Skill allocates the next stable ID, creates the canonical task folder, writes `task-graph.md`, keeps `resolution.md` pending, synchronizes the roadmap, records history when required by local rules, validates the change, and uses the project's review workflow.

The task plan is a research contract, not authorization to solve the task autonomously.

## 10. Work conversationally

A normal continuation is:

```text
Work with me on T002. For this turn, let's start with what Sylow theory forces about the q-Sylow subgroup.
```

The Agent should answer that bounded question, state what was established, and return control at the next meaningful decision point.

When a useful result has been established, preserve it explicitly:

```text
Transcribe the proof we just established as evidence for T002.
Save it as notes/sylow-q-normality.md.
```

When you want adversarial review:

```text
Review the current T002 argument and look for gaps or hidden assumptions.
```

When the accumulated evidence appears sufficient, explicitly request completion:

```text
Evaluate T002 for completion and complete it if the evidence supports an outcome.
```

Negative and inconclusive outcomes remain valid substantive outcomes when supported by the evidence.

## 11. Upgrade deliberately

When a newer Research-Agent release appears, do not silently replace your project pin. Update the installed Skills, test the new release, reconcile any project-local workflow changes, and only then update `research-agent.lock.json` to the new version and source commit.

That separation keeps your research state stable while allowing the reusable Agent/Skill toolchain to evolve.
