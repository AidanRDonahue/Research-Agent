# Architecture

The Research Agent is intentionally split into three runtime layers.

## 1. Agent

`RESEARCH_AGENT.md` defines how the research collaborator behaves: user-directed work, bounded scope, evidence discipline, repository grounding, decision points, completion boundaries, and compatibility awareness.

The Agent answers: **How should the collaborator behave?**

## 2. Skills

Each directory under `skills/` is a standalone reusable Skill for a repeatable operation. Skills are loaded when their trigger matches the user's request.

The Skills answer: **How should this particular operation be performed?**

Current Skills:

- `bootstrap-research-project`: initialize an empty or existing repository as a structured research project.
- `define-research-task`: conduct task intake and publish a new bounded research task.
- `transcribe-research-evidence`: faithfully record specified content as task-local Markdown evidence.
- `review-mathematical-result`: adversarially audit one mathematical claim, proof, derivation, or bound without changing project state.
- `restructure-research-roadmap`: reorganize task relationships and roadmap structure while preserving stable identity and research history.
- `complete-research-task`: evaluate and synthesize a task into its canonical resolution when completion is explicitly requested.
- `validate-research-project`: audit project structure, roadmap/task consistency, evidence boundaries, and applicable mathematical writes.
- `synthesize-research-project`: combine established project results into a coherent higher-level exposition while separating core results from follow-up branches.

## 3. Project repository

An instantiated project contains its own `AGENTS.md`, dictionary, roadmap, task folders, evidence, templates, history, and project-specific artifacts. It may also contain `research-agent.lock.json` to record the external Research-Agent toolchain version it was tested against.

The project repository answers: **What is true here, and what local rules govern this project?**

A project `AGENTS.md` is not the Research Agent itself. It is the local operating contract for that repository. Skills must read it before acting on project state. A toolchain lock is compatibility metadata and never outranks that local contract.

## Versioned distribution

Distribution surrounds the three runtime layers without changing their authority boundaries.

```text
Research-Agent source
    VERSION + skills-manifest.json
                |
                v
scripts/package_skills.py
                |
                +--> one <skill>/skill.zip per Skill
                +--> research-agent-distribution.json
                +--> release bundle + SHA256SUMS
                |
                v
         tagged GitHub release
                |
         +------+------+
         |             |
         v             v
RESEARCH_AGENT.md   installed Skills
         |             |
         +------+------+
                |
                v
        project repository
        research-agent.lock.json
        AGENTS.md + current state
```

The static source manifest records the intended release version and Skill set. The generated distribution manifest records the exact source commit used to build the artifacts. Each packaged Skill also receives generated `DISTRIBUTION.json` metadata.

A release bundle is only a convenience transport for the independent Skill archives. It is not itself a Skill package.

## Dependency direction

```text
User request
    |
    v
Research Agent behavior (`RESEARCH_AGENT.md`)
    |
    +---- matching Skill ----------------+
    |                                    |
    v                                    v
bounded research work             standardized procedure
    |                                    |
    +----------------+-------------------+
                     |
                     v
             project repository
             reads local `AGENTS.md`
             and current project state
```

The important rule is that reusable Skills do not own project state and project repositories do not manually route procedural modules. Versioning makes the reusable tooling observable and reproducible; it does not transfer project authority out of the project repository.
