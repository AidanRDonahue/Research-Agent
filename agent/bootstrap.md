# Repository bootstrap

## Mandated repository structure

The project must use the following top-level structure. These paths and responsibilities are canonical unless this file explicitly permits a project-specific extension.

```text
<Project>/
│
├── README.md
│   └── Project orientation
│       ├── purpose
│       ├── scope
│       ├── repository structure
│       └── working procedure
│
├── AGENTS.md
│   └── Core mandate and module routing
│       ├── repository authority
│       ├── module routing
│       ├── project conventions
│       └── roadmap governance
│
├── agent/
│   ├── bootstrap.md
│   ├── repository-operations.md
│   ├── validation.md
│   ├── node-workflow.md
│   ├── context-scoping.md
│   ├── mathematical-research.md
│   └── transcribe-evidence.md
│
├── dictionary.md
│   └── Canonical project vocabulary
│       ├── terminology
│       ├── identifiers
│       ├── naming conventions
│       └── domain-specific definitions
│
│
├── roadmap.yaml
│   └── CANONICAL PROJECT STATE
│       ├── project metadata
│       ├── ID policy
│       ├── hierarchy policy
│       └── work items
│           ├── parent
│           ├── dependencies
│           ├── status
│           ├── objective
│           ├── method / execution plan
│           ├── deliverables
│           └── outcome branches
│
├── ROADMAP.md
│   └── Human-readable / visual projection of roadmap.yaml
│       └── each item links → its canonical work folder
│
│
├── Tasks/
│   │
│   ├── README.md
│   │   └── Defines the work-item folder convention
│   │
│   ├── T001-<short-title>/
│   │   ├── task-graph.md
│   │   │   └── contract + internal dependency/result graph
│   │   │
│   │   ├── resolution.md
│   │   │   └── canonical completion record / final synthesis
│   │   │
│   │   └── supporting files
│   │       ├── notes/
│   │       ├── data/
│   │       ├── designs/
│   │       ├── experiments/
│   │       ├── scripts/
│   │       ├── references/
│   │       └── other task-specific evidence
│   │
│   ├── T002-<short-title>/
│   │   ├── task-graph.md
│   │   ├── resolution.md
│   │   └── ...
│   │
│   └── ...
│
│
├── Background/
│   └── Shared foundations reused by multiple tasks
│       ├── specifications
│       ├── prior work
│       ├── reference material
│       └── accepted project-wide knowledge
│
├── templates/
│   └── Canonical templates for new work items
│       ├── task-graph.md
│       └── resolution.md
│
├── history/
│   └── roadmap-events.jsonl
│       └── Append-only project-state transition history
│
├── checks/
│   └── project-system-checklist.md
│       └── Manual or automated project validation
│
└── <project-specific artifacts>
    └── Source code, product files, publications,
        models, assets, deployments, etc.
```

The listed governance files and directories, including `agent/`, are part of the project system and must not be replaced by parallel conventions.

Project-specific artifacts may be added at the repository root or in appropriate project-specific directories, but they must not displace or redefine the canonical responsibilities of `README.md`, `AGENTS.md`, `agent/`, `dictionary.md`, `roadmap.yaml`, `ROADMAP.md`, `Tasks/`, `Background/`, `templates/`, `history/`, or `checks/`.

Do not create competing locations for canonical project state, task contracts, task resolutions, shared foundations, templates, or project-state history.
