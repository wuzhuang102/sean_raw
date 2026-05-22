---
source_type: "concept-notes"
captured: "2026-05-22"
scope: "Compact agent skill basic concepts"
---

## User Request

将 agent skill 基础概念缩减到一个标题下，把页面主体空间留给具体 skill 介绍。

## Sources Kept

- OpenAI `openai/skills` GitHub repository: https://github.com/openai/skills
  - Defines Agent Skills as folders of instructions, scripts, and resources that agents can discover and use for specific tasks.
- Claude.ai Skills overview: https://claude.com/docs/skills/overview
  - Defines skills as directories containing instructions, scripts, and resources.
  - Explains `SKILL.md` activation and progressive disclosure.
- Claude Code skills docs: https://docs.claude.com/en/docs/claude-code/skills
  - Explains `SKILL.md`, frontmatter, skill locations, invocation, and supporting files.
- Anthropic guide PDF: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
  - Describes the required/optional folder structure and repeatable workflow use cases.

## Concepts Preserved

- A skill is a reusable task capability package.
- The core file is usually `SKILL.md`.
- Optional resources include scripts, references, assets, templates, and examples.
- Skills use progressive loading: metadata first, full instructions when matched, supporting resources when needed.
- Skills are best for repeatable workflows, fragile procedures, domain-specific knowledge, and reusable team practices.
- Third-party skills should be reviewed before installation or use.
