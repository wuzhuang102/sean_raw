# Browser Use source capture

- captured: 2026-05-25
- GitHub repository: https://github.com/browser-use/browser-use
- documentation: https://docs.browser-use.com/
- website: https://browser-use.com/

# GitHub repository snapshot

Repository: `browser-use/browser-use`.

The repository describes Browser Use as a way to make websites accessible for AI agents and automate online tasks. It is an open-source Python browser automation framework with cloud-hosted infrastructure options.

Captured repository metadata:

- license: MIT
- primary language: Python
- repository state at capture: public; 95.3k stars; 10.7k forks; 9,281 commits
- latest release shown: `0.12.8`, dated 2026-05-23
- notable folders/files shown: `browser_use/`, `examples/`, `skills/`, `docker/`, `tests/`, `README.md`, `pyproject.toml`

README highlights:

- Browser Use offers both an open-source agent and Browser Use Cloud.
- The local quickstart uses Python 3.11+ and `uv add browser-use`.
- The basic agent API wires together `Agent`, `Browser`, and an LLM provider such as `ChatBrowserUse`, Google, or Anthropic.
- Cloud is positioned for scalable, stealth-enabled browser automation with proxy rotation, CAPTCHA solving, persistent filesystem, memory, and many integrations.
- The CLI supports persistent browser automation commands such as open, state, click, type, screenshot, and close.
- Browser Use also publishes a Claude Code skill for AI-assisted browser automation.
- The FAQ says the open-source library is free, with the user choosing an LLM provider or local model; Browser Use services have separate terms and privacy policy.
- Authentication examples include using real browser profiles and syncing an auth profile to remote browsers.

# Documentation snapshot

The cloud quickstart describes Browser Use as state-of-the-art AI browser automation with stealth browsers, CAPTCHA solving, residential proxies, and managed infrastructure.

The cloud SDK distinguishes:

- Agent: `sessions.create()` / `run()`; runs an AI task with task, model, proxy, profile, recording, workspace, keep-alive.
- Browser: `browsers.create()`; exposes a raw browser over CDP with options such as proxy, profile, recording, screen size, and timeout.

# Interpretation notes

Browser Use is best understood as a dynamic web-use agent framework: the model observes the browser state, plans actions, and executes through browser automation. This contrasts with AOT/compiled-workflow tools such as Freu CLI, which try to move repeated navigation out of the model loop.
