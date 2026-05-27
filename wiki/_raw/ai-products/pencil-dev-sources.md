# Pencil.dev source notes

Captured: 2026-05-26

## Public sources checked

- Official site: https://www.pencil.dev/
- Documentation home: https://docs.pencil.dev/
- AI integration: https://docs.pencil.dev/getting-started/ai-integration
- Design to code: https://docs.pencil.dev/design-and-code/design-to-code
- .pen files: https://docs.pencil.dev/core-concepts/pen-files
- Code on Canvas: https://docs.pencil.dev/core-concepts/code-on-canvas
- Pencil CLI: https://docs.pencil.dev/for-developers/pencil-cli
- Terms of use: https://www.pencil.dev/terms-of-use

## Source facts

- Pencil positions itself as an agent-driven MCP canvas and AI design product where design files live in the codebase.
- The product has multiple entry points: IDE extensions, desktop apps, and a CLI.
- The core file model is `.pen`, described by the docs as JSON-based, portable, and Git-friendly.
- The AI integration uses MCP so assistants can read and modify `.pen` files. The docs name Claude Code, Claude Desktop, Cursor, Windsurf, Codex CLI, Antigravity IDE, and OpenCode CLI as supported assistant surfaces.
- The design-to-code flow is two-way: design can be generated into code, and existing code can be imported back into Pencil.
- Code on Canvas uses script nodes linked to `.js` files to render generated layers for structured, data-driven, or parameterized design elements.
- The CLI can create or modify `.pen` files with prompts, export designs, run interactively, and call MCP tools directly. It requires authentication for agent operations and can use CLI keys for CI/CD.
- The terms of use describe Pencil as a product by High Agency, Inc. and say generated outputs belong to the user subject to third-party rights; they also state Inputs/Outputs are not stored or recorded on Pencil servers and are not used for model training unless the user opts in.

## Link verification

- `curl -I https://www.pencil.dev/` returned HTTP 200 on 2026-05-26.
- `curl -I https://docs.pencil.dev/` returned HTTP 200 on 2026-05-26.
- `curl -I https://docs.pencil.dev/getting-started/ai-integration` returned HTTP 200 on 2026-05-26.
