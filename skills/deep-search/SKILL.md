---
name: deep-search
description: >-
  Performs thorough, multi-phase codebase investigation: broad ripgrep/glob
  discovery, import/call-chain tracing, and synthesized findings with file:line
  citations. Use when the user asks for deep search, full codebase scan, "where is
  X used", architecture mapping, impact analysis, or anything requiring exhaustive
  repo exploration beyond a quick lookup. Do not use for single known file paths,
  trivial one-line greps, or tasks that only need web/docs search.
disable-model-invocation: true
---

# Deep Search

You are in **deep search mode**. The user wants exhaustive repo understanding, not a quick answer.

## Goal

Map how a symbol, pattern, feature, or concept appears across the codebase: definitions, callers, config, tests, and conventions.

## Inputs

Parse from the user message (or skill args):

- **Target**: symbol, string, regex, feature name, or concept
- **Scope** (optional): directory, package, or layer (e.g. `src/api`, `frontend`)
- **Depth** (optional): `quick` | `standard` (default) | `exhaustive`

## Workflow

### Phase 1 — Broad discovery

Run searches **in parallel** when possible:

1. Exact match: symbol / string / error message
2. Variants: camelCase, snake_case, kebab-case, abbreviations, env keys, route paths
3. File discovery: glob by likely names (`*Auth*`, `*middleware*`, etc.)
4. Config & infra: `*.json`, `*.yaml`, `*.toml`, `Dockerfile`, CI, env examples

Prefer `rg` / grep tools over reading whole trees. Cap noisy hits; refine with path or file type filters.

### Phase 2 — Deep dive

For each high-signal hit:

1. Read the defining file and surrounding context
2. Trace **imports / exports** and re-exports (barrel files)
3. Find **callers** and **callees** (who uses this? what does it depend on?)
4. Check **tests**, **fixtures**, and **mocks** for usage examples
5. Note framework hooks: routes, middleware, DI, event handlers, codegen

Stop when:

- Primary implementation and main consumption paths are identified, or
- Diminishing returns (duplicate wrappers, generated code only), or
- User scope is satisfied

For `exhaustive`, also scan docs, ADRs, and comment-only references.

### Phase 3 — Synthesize

Produce a structured report (see template). Every claim should cite `path:line` or a tight line range.

## Rules

- **Read before asserting.** Do not infer behavior from names alone.
- **Prefer evidence over volume.** Fewer cited facts beat long file lists.
- **Respect ignore files.** Do not search `node_modules`, `venv`, `.git`, build output unless asked.
- **Monorepos**: search per package when layout suggests it; call out package boundaries.
- **Ambiguity**: if multiple unrelated matches share a name, separate them into distinct sections.
- **No edits** unless the user asked to change code; this skill is investigation-only.

## Output template

```markdown
## Summary
<1–3 sentences: what the target is and where it lives>

## Primary locations
| Role | Path | Notes |
|------|------|-------|
| Definition | `path:line` | … |
| Main entry | `path:line` | … |

## Call graph / data flow
<short bullets or mermaid if helpful>

## Related files
- `path` — consumer / config / test / …

## Usage patterns
- How teams use this (conventions, required order, side effects)

## Key insights
- Gotchas, feature flags, env deps, breaking edges

## Gaps
<what was not found or needs human confirmation>
```

## Tool hints (Codex)

- Ripgrep/glob for discovery; read files for context
- Shell only when repo scripts document search helpers
- Web search **only** if the target is external (library API, RFC) — not for in-repo symbols

## Slash command

Users may invoke: `$deep-search <query>` or `/deep-search <query>`.
