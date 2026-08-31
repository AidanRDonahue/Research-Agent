# Research Project Template

Use this reference when bootstrapping a target repository. Replace angle-bracket placeholders with user-supplied project information and preserve existing compatible project artifacts.

## Canonical top-level structure

```text
<Project>/
|-- README.md
|-- AGENTS.md
|-- dictionary.md
|-- roadmap.yaml
|-- ROADMAP.md
|-- research-agent.lock.json    # when concrete distribution metadata is available
|-- Tasks/
|   |-- README.md
|   `-- T001-<central-question-slug>/
|       |-- task-graph.md
|       |-- resolution.md
|       `-- background/
|-- templates/
|   |-- task-graph.md
|   `-- resolution.md
|-- history/
|   `-- roadmap-events.jsonl
|-- checks/
|   `-- project-system-checklist.md
`-- <project-specific artifacts>
```

## Project-local AGENTS.md baseline

The target repository's `AGENTS.md` should define local authority and state conventions, not the general Research Agent personality and not a manual module-routing table.

At minimum record:

- repository state is authoritative over model memory;
- authority order: `AGENTS.md`, `dictionary.md`, current research artifacts, `roadmap.yaml`, `ROADMAP.md`, append-only history;
- `dictionary.md` is the notation/terminology authority;
- `roadmap.yaml` is canonical structured roadmap state;
- `ROADMAP.md` states the central research question outside its Mermaid block, omits `T001` from the Mermaid graph, and makes every Mermaid task node a clickable hyperlink to its canonical GitHub task folder;
- node-scoped context normally includes only the current task, its conceptual parent when it is a child node, declared dependencies, required cross-links, and directly relevant task-local evidence;
- every task has exactly one canonical `Tasks/<STABLE-ID>-<slug>/` folder containing `task-graph.md` and a pending-or-completed `resolution.md`;
- stable IDs are monotone and never reused; new `display_index` values default to the stable ID unless the user or project specifies otherwise;
- `T001` is the special central-question task, has no conceptual parent, and is not a Mermaid roadmap node;
- every roadmap task other than `T001` is explicitly classified as either a root node with no conceptual parent or a child node with exactly one conceptual parent; conceptual-parent and dependency graphs are acyclic;
- `T001` is not used as a conceptual parent in the roadmap graph; a task that would otherwise be a direct child of the central question is a roadmap root node;
- task-specific evidence remains task-local, while genuinely global background material is stored inside the canonical `T001` folder, normally under `background/`;
- ordinary task work is user-directed and does not authorize autonomous completion;
- project-authored mathematical operations use `\mathrm{...}` rather than `\operatorname{...}` unless the dictionary records another convention;
- `research-agent.lock.json`, when present, records external toolchain compatibility and never overrides project-local research authority; and
- substantive repository mutations use a scoped branch and reviewable pull request unless the user explicitly authorizes another write path.

## Toolchain lock

When the installed bootstrap Skill exposes concrete generated `DISTRIBUTION.json` metadata, create `research-agent.lock.json` with schema version 1 and record:

- Research-Agent source repository;
- release version;
- release tag;
- exact source commit; and
- the core Skills the project expects to use.

If concrete distribution metadata is unavailable, do not guess or infer a version/commit from memory. The project may remain temporarily unpinned; report that limitation so the user can create the lock from the release's `research-agent-distribution.json` later.

The lock is deployment/compatibility metadata. It does not change the authority order for research state.

## Central research task

Create `T001` for the overarching research question. It may remain unresolved while the roadmap is developed and should not be treated as resolved until the project-level synthesis supports the central question.

A new task folder uses the project template for `task-graph.md` and `resolution.md`. The `T001` `resolution.md` begins with an explicit pending notice and must not imply that the overarching question is solved. Store global background material inside the `T001` folder, normally under `background/`.

## Task contract baseline

A `task-graph.md` should record:

- stable ID and display index;
- title, type, and status;
- roadmap role: central task (`T001`), root node, or child node;
- conceptual parent only for a child node;
- relation to parent and effect on parent only when a conceptual parent exists;
- uncertainty reduced / question answered;
- exact dependencies and cross-links;
- objective;
- included and excluded scope;
- assumptions and conventions;
- bounded method;
- stopping rules;
- success, negative, and realistic inconclusive branches;
- independent validation; and
- a Mermaid result-dependency graph based on actual evidence/results rather than generic process steps.

## Roadmap baseline

`roadmap.yaml` is the canonical structured state. It should retain `T001` as the central research task even though the visual graph omits it. For every other task, record whether it is a roadmap root or child; record a conceptual parent only for child nodes.

`ROADMAP.md` should state or link the central research question outside the Mermaid block. The Mermaid graph must omit `T001`. Every task node shown in the Mermaid graph must be clickable and target the corresponding canonical GitHub task folder, using a URL of the form:

```text
https://github.com/<OWNER>/<REPOSITORY>/tree/<DEFAULT-BRANCH>/Tasks/<STABLE-ID>-<slug>
```

Use Mermaid `click` directives or an equivalent GitHub-rendered Mermaid hyperlink mechanism. Keep the link target synchronized when a task folder path changes.

Do not prewrite future branches. Initialize only `T001` unless the user has explicitly authorized additional tasks.

## Validation baseline

Create `checks/project-system-checklist.md` covering at least:

- required files/directories;
- roadmap/task agreement;
- unique monotone stable IDs;
- root/child classification, parent validity for child nodes, and parent/dependency acyclicity;
- exclusion of `T001` from the Mermaid graph;
- clickable GitHub links for every Mermaid task node, targeting the corresponding canonical task folder;
- one canonical folder per task;
- required task files;
- global background placement under `T001`;
- pending versus completed resolution state;
- evidence/result graph consistency;
- referenced evidence existence;
- terminology and notation consistency;
- append-only history validity;
- Research-Agent lock validity when the project uses a compatibility pin; and
- repository-specific tests or CI when applicable.
