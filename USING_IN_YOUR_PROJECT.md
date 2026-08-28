# Use Research-Agent in Your Own Project

This tutorial is self-contained. It takes you from the Research-Agent repository to a version-pinned research project and then shows the normal research workflow and the safe upgrade path.

## 1. Understand what you are installing

Research-Agent has three runtime layers and one distribution layer:

```text
Research Agent behavior
    RESEARCH_AGENT.md
            |
            v
Installed Skills
    one reusable procedure per Skill
            |
            v
Your project repository
    local rules + research state

Versioned distribution
    packages and pins the Agent/Skill toolchain
```

The project repository is authoritative for its own research. A Skill supplies a reusable procedure; it does not own your project's task IDs, notation, evidence, roadmap, or completion state.

## 2. Choose a released version

For repeatable work, use a tagged Research-Agent release rather than installing arbitrary files from `main`.

A release contains:

- `research-agent-skills-v<VERSION>.zip` — a convenience bundle containing the independent Skill packages;
- `research-agent-distribution.json` — the exact version, source commit, and package checksums/metadata; and
- `SHA256SUMS` — integrity checksums for the published artifacts.

The source file `VERSION` and `skills-manifest.json` describe the release intended by the source tree. The generated distribution manifest is stronger evidence for an installed release because it records the exact build commit.

## 3. Extract the Skill bundle

Extract `research-agent-skills-v<VERSION>.zip` locally. You will get a layout like:

```text
research-agent-distribution.json
bootstrap-research-project/
    skill.zip
complete-research-task/
    skill.zip
define-research-task/
    skill.zip
restructure-research-roadmap/
    skill.zip
review-mathematical-result/
    skill.zip
synthesize-research-project/
    skill.zip
transcribe-research-evidence/
    skill.zip
validate-research-project/
    skill.zip
```

The outer release bundle is **not** a Skill. Each inner `skill.zip` is an independent Skill package and should be installed separately.

## 4. Configure the Research Agent behavior

Open `RESEARCH_AGENT.md` from the same release tag and use it as the persistent instructions for the GPT/agent that will conduct the research.

Do not use this repository's root `AGENTS.md` as your research-agent prompt. The root `AGENTS.md` governs maintenance of the Research-Agent source repository itself.

Your project will receive its own project-local `AGENTS.md` during bootstrap.

## 5. Install the core Skills

Install the independent `skill.zip` packages from the release bundle in ChatGPT's Skills interface. For the complete workflow, install all core Skills:

- `bootstrap-research-project`
- `define-research-task`
- `transcribe-research-evidence`
- `review-mathematical-result`
- `restructure-research-roadmap`
- `complete-research-task`
- `validate-research-project`
- `synthesize-research-project`

Each package contains generated `DISTRIBUTION.json` metadata identifying the exact Research-Agent release and source commit it came from.

Installing a newer GitHub source file does not automatically update a Skill already installed in ChatGPT. Treat installation/update as a deployment step.

## 6. Connect the repository you want to research

Give the agent access to the GitHub repository that will store your project. The repository may be empty or may already contain project material.

Use a repository you control if you expect the Agent to publish task files or other durable state. Read-only access is sufficient for research that does not require repository writes.

## 7. Bootstrap your project

Start with a bounded root question. For example:

```text
Initialize OWNER/REPOSITORY as a Research-Agent project around the question:
"Which finite groups of order n occur up to isomorphism?"

Use the papers already in Background/ as supplied background.
```

The `bootstrap-research-project` Skill should inspect the repository first, preserve compatible existing artifacts, and create the project-local research system. A typical project contains:

```text
README.md
AGENTS.md
dictionary.md
roadmap.yaml
ROADMAP.md
Tasks/
Background/
templates/
history/
checks/
research-agent.lock.json    # when concrete distribution metadata is available
```

The root task begins pending. Bootstrap does not solve it and does not prewrite an entire solution roadmap.

## 8. Pin the Research-Agent distribution

If the installed bootstrap Skill can read its generated `DISTRIBUTION.json`, it should use that concrete metadata to create `research-agent.lock.json` in the project. The lock should record the exact repository, release version, release tag, source commit, and Skills expected by the project.

If your environment does not expose the packaged metadata, do not guess the commit. Instead:

1. open the release's `research-agent-distribution.json`;
2. copy `templates/research-agent.lock.example.json` from the same Research-Agent release into your project as `research-agent.lock.json`;
3. replace the placeholder source commit with the exact `source_commit` from the distribution manifest; and
4. remove any Skill from `required_skills` only if your project deliberately does not depend on that procedure.

The lock is **compatibility metadata**. Your project's `AGENTS.md`, dictionary, tasks, evidence, and roadmap remain the authorities for the research itself.

## 9. Verify a pin when you have a Research-Agent checkout

If you have cloned Research-Agent, compare a project lock with a downloaded release manifest using:

```bash
python scripts/check_project_compatibility.py \
  /path/to/your-project/research-agent.lock.json \
  --distribution /path/to/research-agent-distribution.json
```

A successful check reports the pinned version, source commit, and required Skill count. A mismatch exits nonzero and reports the exact difference.

## 10. Work on research conversationally

After bootstrap, ordinary research does not require a special command. Name the task and the bounded question you want addressed:

```text
Work with me on T002. For this turn, determine what Sylow theory forces about the q-Sylow subgroup. Do not continue into the semidirect-product classification yet.
```

The Agent should read the project's current `AGENTS.md`, load the relevant local context, answer that bounded question, distinguish established results from uncertainty, and return control to you.

The task contract is not permission to autonomously finish the task.

## 11. Invoke standardized workflows with natural language

Ask for the operation you want. Installed Skill metadata handles selection.

To define a task:

```text
Define a new task under T002 for determining when the nontrivial semidirect product exists. Start the intake conversation; do not solve the task.
```

To review mathematics:

```text
Review the current T002 classification lemma adversarially. Check hidden hypotheses and the exact proved scope.
```

To preserve evidence:

```text
Transcribe the verified Sylow argument as evidence for T002 and save it as notes/sylow-q-normality.md.
```

To restructure the roadmap:

```text
Restructure this branch so the obstruction becomes a sibling task rather than a subcase. Preserve stable IDs and history.
```

To complete a task:

```text
Evaluate T002 for completion and complete it only if the current evidence supports one of its declared outcomes.
```

To validate a project change:

```text
Validate this branch against the project's current AGENTS.md and project checklist. Report failures without repairing them unless I ask.
```

To synthesize established work:

```text
Synthesize the completed classification tasks into a paper-level outline while preserving each result's exact hypotheses.
```

## 12. What gets stored where

Keep the separation explicit:

```text
AidanRDonahue/Research-Agent
    reusable Agent + Skill source + release tooling

ChatGPT Skills library
    installed executable copies of the Skill packages

Your project repository
    project-local rules, terminology, tasks, evidence, roadmap, history
```

Do not copy all of `skills/` into your project merely to make the project work. Vendoring is possible when you deliberately need a self-contained source snapshot, but the normal model is an external versioned toolchain plus a project lock.

## 13. Upgrade safely

Do not make your project follow `Research-Agent/main` automatically.

When a new release appears:

1. read its release notes;
2. download the new bundle and `research-agent-distribution.json`;
3. identify which Agent/Skill contracts changed;
4. install or update the corresponding Skill packages in ChatGPT;
5. test the new release against a project branch or representative workflow;
6. compare the new distribution with the project's existing lock;
7. reconcile any project-local changes required by the new workflow; and
8. update `research-agent.lock.json` only after you intentionally accept the new release.

A version mismatch is a review signal, not permission for an automatic migration.

## 14. Package the current source yourself

If you are developing Research-Agent rather than consuming a tagged release, clone the repository and run:

```bash
python scripts/package_skills.py --output dist
```

The script validates the complete Skill set against `skills-manifest.json`, checks each Skill entrypoint and UI metadata, enforces the 25 MB per-Skill archive limit, and creates deterministic packages under `dist/`.

A typical development output is:

```text
dist/
    research-agent-distribution.json
    research-agent-skills-v<VERSION>.zip
    SHA256SUMS
    bootstrap-research-project/skill.zip
    ...
```

Pull requests run the same packaging path in GitHub Actions. Pushing an exact `v<VERSION>` tag after review triggers release publication.

## 15. Troubleshooting

**A Skill does not trigger.** Verify that the individual Skill is installed, not merely present in GitHub or inside the unextracted release bundle. Then make the request use the operation named in the Skill's description.

**The project says its Research-Agent version is different.** Compare `research-agent.lock.json` with the distribution manifest for your installed packages. Do not silently overwrite the lock.

**The Skill and project disagree about task IDs or notation.** The project-local `AGENTS.md` and its declared project authorities control project-specific behavior. Surface the conflict rather than letting a generic Skill rewrite local conventions.

**You edited a Skill on GitHub but ChatGPT still behaves the old way.** Source edits are not deployments. Package a new distribution and update the installed Skill.

**You only want ordinary research, not a repository mutation.** Ask the bounded research question directly. Specialized Skills are for repeatable procedures; they are not required for every reasoning turn.

## 16. The workflow in one picture

```text
Research-Agent tagged release
    |
    +-- RESEARCH_AGENT.md ----------> persistent agent behavior
    |
    +-- per-Skill skill.zip --------> installed ChatGPT Skills
    |
    `-- distribution manifest ------> research-agent.lock.json
                                         in your project

User request
    |
    v
Research Agent
    |
    +-- ordinary bounded reasoning
    |
    `-- matching installed Skill
             |
             v
       reads project AGENTS.md
             |
             v
       acts on current project state
```

That is the intended operating model: one versioned reusable toolchain, installed Skills for repeatable procedures, and a project repository that remains the authoritative record of the research.
