# Freu CLI / Freu AI source capture

- captured: 2026-05-25
- primary Product Hunt URL: https://www.producthunt.com/products/freu-cli
- official site: https://www.freu.ai/
- GitHub repository: https://github.com/freu-ai/freu-cli

# Product Hunt snapshot

Product Hunt page title: Freu AI.

The page positions Freu AI as a Mac AI agent for automating desktop apps with natural language. It describes the workflow as: observe the UI once, compile a reusable cross-app workflow, and run future executions locally through a deterministic DSL.

Captured product metadata:

- category: AI Workflow Automation
- tags shown: Artificial Intelligence, GitHub, Business Intelligence
- pricing label: Free Options
- company info links: freu.ai and GitHub
- launch year shown: 2026
- page state at capture: Launching today; day rank #3; 207 points; 370 followers

Maker comment highlights:

- The stated problem is that traditional RPA is brittle and vision agents can be expensive for repeated UI navigation.
- Freu's proposed architecture is Ahead-of-Time compilation for OS-level tasks: a cloud vision model analyzes a demonstrated workflow once and compiles it into a reusable DSL.
- Future execution is described as local deterministic execution, reducing repeated cloud token use and latency.
- Semantic UI is described as anchoring actions to UI meaning rather than fixed screen coordinates.
- The open-source component launched with the Product Hunt page is `freu-cli`, described as the DOM-based browser automation engine.
- Current anomaly handling, according to a maker reply, pauses safely when unexpected dialogs appear and may use a cloud model for recovery today; a local vision execution engine is described as planned.

# GitHub repository snapshot

Repository: `freu-ai/freu-cli`.

The README describes Freu CLI Browser Edition as the first release of the Freu AI automation suite. It focuses on high-efficiency web orchestration and reducing repeated agent token use by compiling recorded browser sessions into reusable deterministic commands.

Captured repository metadata:

- license: AGPL-3.0
- language: Python
- repository state at capture: public; 17 stars; 1 fork; 4 commits
- folders/files shown: `assets/`, `docs/`, `examples/Github`, `src/freu_cli`, `tests`, `README.md`, `CHANGELOG.md`, `pyproject.toml`, `LICENSE`

README highlights:

- The architecture is framed as AOT compilation rather than JIT interpretation.
- Learn flow: a human records a browser workflow; Freu filters DOM noise and compiles raw events into a semantic DSL, `SKILL.md`, and JSON command files.
- Run flow: an agent invokes the generated command instead of repeatedly reasoning over DOM or visual context.
- Stable targeting is based on "constellations": semantic anchors plus surrounding DOM context, pruned to avoid brittle generated classes, IDs, and attributes.
- Data extraction objectives can be compiled into element text or attribute retrieval steps with command outputs.
- `freu-cli learn` uses an LLM selected by `LLM_MODEL`, defaulting to `gpt-5.1` in the README, routed through LiteLLM.
- Supported integrations listed include OpenClaw, Claude Code, Codex CLI, Cursor, and Hermes skill directories.
- Runtime failure output is designed to report completed steps, pending step, and reason in an agent-friendly shape.
