# agent-computer-use source capture

- captured: 2026-05-25
- documentation: https://www.agent-computer-use.dev/
- GitHub repository: https://github.com/kortix-ai/agent-computer-use
- note: user requested "compute-use"; search results did not show a stable primary project with that exact name. The closest verified tool is `agent-computer-use`, whose CLI command/package is `agent-cu`.

# Documentation snapshot

The docs identify `agent-computer-use` as a computer use CLI for AI agents. It lets users and agents control desktop apps from the terminal: click buttons, type into fields, and read screen state from one CLI.

Core workflow:

- Snapshot: capture interactive elements from an app; each element receives a ref such as `@e5`.
- Act: click, type, read text, or otherwise operate using refs.
- Re-snapshot: refresh refs after the UI changes.

The docs say the tool reads the accessibility tree used by screen readers and exposes buttons, text fields, and menu items to the agent. Example use cases include maps search, Slack messages, forms, calculator operations, extracting booking data, moving desktop app data into spreadsheets, setup wizards, and YAML workflows.

# GitHub repository snapshot

Repository: `kortix-ai/agent-computer-use`.

Captured repository metadata:

- license: MIT
- primary language: Rust
- repository state at capture: public; 20 stars; 9 forks; 70 commits
- latest release shown: `agent-cu@0.1.1`, dated 2026-04-16
- notable folders/files shown: `cli/`, `docs/`, `skills/agent-computer-use`, `docker/`, `README.md`, `package.json`, `LICENSE`

README highlights:

- The project positions itself as one CLI for desktop apps on macOS, Linux, Windows, and Electron.
- Its comparison table contrasts accessibility-driven control with vision-based computer-use systems and pixel automation.
- It claims zero per-action vision token cost because it uses accessibility and CDP primitives instead of screenshots.
- Installation is through `npm install -g agent-cu` or equivalent package managers; precompiled binaries are provided for macOS, Linux, and Windows.
- After install, users grant accessibility permissions and can run `agent-cu check-permissions`.
- It ships as a skill on skills.sh for Claude Code, Cursor, Codex, Copilot, OpenCode, Cline, and other agents.
- Core commands include app discovery, snapshots, accessibility tree reads, selectors, clicks, typing, key presses, scrolling, drag, window management, screenshots, waits, verification, batch execution, YAML workflows, and an interactive TUI explorer.
- Electron apps can use automatic CDP support, merging DOM access with the native shell.
- Output is JSON by default for agent consumption.
- Architecture is Rust CLI plus platform backends: macOS AXUIElement/CGEvent, Linux AT-SPI2, Windows UIAutomation, and a CDP bridge for Electron.
- Platform support is marked Preview for macOS, Electron, Windows, and Linux.

# Interpretation notes

agent-computer-use is best understood as a local deterministic desktop-control primitive for agents. It is closer to `pyautogui` plus accessibility/CDP selectors than to a full autonomous planner. The LLM remains outside the tool: it reads snapshots, chooses refs/selectors, and asks the CLI to act.
