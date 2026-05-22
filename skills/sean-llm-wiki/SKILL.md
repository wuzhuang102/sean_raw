---
name: sean-llm-wiki
description: Build and maintain a persistent LLM-written full-stack engineering wiki from raw sources. Use when the user wants to ingest files, notes, URLs, transcripts, research, conversations, or project context into a structured wiki under wiki/, keep immutable raw inputs outside generated pages, update markdown pages with provenance and cross-links, lint the knowledge base, answer questions from the wiki, or export the wiki as markdown and a single self-contained HTML file.
disable-model-invocation: true
---

## Operating Model

Treat the wiki as a compiled knowledge layer between raw sources and answers. The target shape is a full-stack engineering knowledge base: useful for human browsing, LLM retrieval, interview preparation, architecture work, debugging, and project memory.

- Keep raw sources immutable under `<project>/wiki/_raw/`, grouped into semantic subdirectories such as `frontend/`, `backend/`, `infra/`, `ai-engineering/`, `projects/`, or `sources/`. Do not use `<project>/raw/` for this skill.
- Maintain generated wiki pages in `<project>/wiki/`.
- Prefer markdown as the canonical format.
- Generate single-file HTML exports only from the markdown wiki; do not edit exported HTML as source.
- Update `wiki/index.md` and `wiki/log.md` on every ingest, reading-note update, query-to-page, lint pass, or export. Keep `wiki/log.md` newest-first, grouped by year and month.
- Cite raw sources and existing wiki pages for non-obvious claims.
- Ask before overwriting user-authored pages or resolving contradictions that require judgment.

Use `$HOME/Desktop/demo/sean_raw` as the default project root. The maintained wiki lives under `$HOME/Desktop/demo/sean_raw/wiki`. Raw sources should live under semantic subdirectories of `$HOME/Desktop/demo/sean_raw/wiki/_raw`. Expand `~` or `$HOME` at runtime instead of hard-coding the current username. If the user explicitly points to another root for a specific task, use that root for that task only.

## Directory Layout

Create this structure on first use:

```text
wiki/
  index.md
  log.md
  _raw/
    frontend/
    backend/
    ai-engineering/
    infra/
    projects/
    sources/
  maps/
  topics/
    frontend/
    backend/
    ai-engineering/
    infra/
  patterns/
  playbooks/
  decisions/
  projects/
  comparisons/
  glossary/
  reading-notes/
    index.md
    technology/index.md
    work/index.md
    product/index.md
    business/index.md
    personal/index.md
    misc/index.md
  exports/
  meta/
```

Use semantic directories because the wiki is consumed by humans and LLMs by intent, not by source order.

- `maps/`: navigation pages for major domains and workflows.
- `_raw/`: immutable raw inputs, grouped by domain or source family. Prefer the same high-level domains as generated pages; use `sources/` for mixed external references that do not fit one domain.
- `topics/`: durable technical knowledge and mental models.
- `patterns/`: reusable engineering designs, tradeoffs, and failure modes.
- `playbooks/`: step-by-step operating guides for debugging, shipping, and maintenance.
- `decisions/`: architecture decision records and technical choices.
- `projects/`: project-specific context, architecture, incidents, and lessons.
- `comparisons/`: technology or design option comparisons.
- `glossary/`: short concept definitions with links to deeper pages.
- `reading-notes/`: lightweight reading records grouped by one primary category. Use category `index.md` files instead of one page per source.
- `exports/`: generated outputs such as `wiki.html`, PDF-ready markdown, or slide markdown.
- `meta/`: wiki maintenance notes, taxonomy decisions, lint reports, unresolved contradictions.

For detailed filing rules, read `references/wiki-taxonomy.md`.

## Page Conventions

Use concise YAML frontmatter on generated markdown pages. The readable page title is derived from the filename or index entry, so do not add a separate level-1 heading just to repeat the page title. Start the generated body at level-1 headings for real content sections (`# Section`), then use `##`, `###`, and lower levels for subsections. Do not duplicate the filename as a `title` field unless a downstream integration explicitly requires it.

```yaml
---
type: "map|topic|pattern|playbook|decision|project|comparison|glossary|meta"
status: "draft|active|contested|stale|archived"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
sources:
  - "../../_raw/infra/example.md"
tags: []
---
```

Prefer stable, readable filenames: lowercase words separated by hyphens for English, or clear Chinese names when Chinese better matches the material. Keep one major concept per page. Use wiki links or normal relative markdown links consistently with the surrounding wiki. Add a `# Sources` section when a page aggregates claims from multiple raw files.

For user-facing sources, cite links a reader can open directly: official docs, GitHub files/directories, papers, standards, or stable external pages. Do not make the page body say "source: raw" or point readers only to `wiki/_raw/...`; raw files are internal provenance for frontmatter, logs, and maintenance. When using web links, verify important links before writing them, preferably with `curl -I` or an equivalent check, and replace broken or unstable marketplace mirrors with the most direct stable source.

When claims conflict, mark affected pages `status: contested`, add a short `# Contested Claims` section, and log the conflict in `meta/contradictions.md`. Do not silently choose a winner unless the user gives a rule.

## Workflows

### Capture Reading Notes

Use this workflow when the user asks to save, file, summarize, or remember an article, book, paper, doc, transcript, video, or link as reading material. This is distinct from durable wiki synthesis.

1. Put the reading record under `reading-notes/`, not under `topics/`, `patterns/`, or other durable knowledge directories by default.
2. Use one primary category only. Prefer these categories unless the user gives a stronger local taxonomy:
   - `reading-notes/technology/index.md`: engineering, AI, architecture, tools, technical papers, and implementation writeups
   - `reading-notes/work/index.md`: management, collaboration, project retrospectives, organizational process, and career material
   - `reading-notes/product/index.md`: product design, UX, growth, requirements, and user research
   - `reading-notes/business/index.md`: companies, industries, commercial models, markets, and strategy
   - `reading-notes/personal/index.md`: personal growth, learning systems, life systems, and non-work methods
   - `reading-notes/misc/index.md`: material that does not yet have a stable home
3. Do not duplicate the same source across multiple category files. Use `tags` for cross-category attributes.
4. Inside each category `index.md`, keep entries newest-first by record date, grouped by year and month:

```markdown
# 2026

## 2026-05

### 2026-05-22 | Source title
- link: https://example.com/source
- summary: One to three concise sentences. Use the user's summary when provided; otherwise summarize from the fetched or provided content.
- tags: `tag-one`, `tag-two`
```

5. Use the record date, not the original publication date, for the year/month grouping. Mention the publication date in the summary only when it matters.
6. Keep reading-note entries lightweight. Do not create a detailed page per source unless the user explicitly asks for one.
7. If the user provides only a link, fetch readable content before summarizing when tools allow it. Use `curl` or other available local commands for ordinary web links. For Lark/Feishu document links, use the `lark-doc` skill to fetch readable content first; do not duplicate Lark CLI command details here.
8. If the link cannot be accessed, requires permission, is too dynamic to fetch, or yields insufficient content, record the link and title when available, set `summary` to `待补充`, and mention the access problem briefly. Do not infer a summary from only the URL or title.
9. When the user gives a special instruction such as "沉淀观点", "整理到知识库", "更新相关文档", "归纳成长期知识", "加入 wiki", "整理重要观点", or "提炼到合适文档", first write or update the reading-note entry, then update the most relevant durable wiki pages. Prefer existing pages found through `wiki/index.md` and `rg`; create new `topics/`, `patterns/`, `playbooks/`, `decisions/`, or other durable pages only when no suitable page exists.
10. When durable pages are updated from a reading note, add a `distilled` line to the reading-note entry:

```markdown
- distilled: `topics/ai-engineering/example.md`, `patterns/example.md`
```

11. Update `wiki/index.md` so it includes `# Reading Notes` and links to the category indexes that exist. Update `wiki/log.md` with action `reading-note`; consolidate same-day reading-note work when it is part of the same thread.

### Ingest Raw Sources

1. Put or confirm the raw file under a semantic subdirectory of `wiki/_raw/`, such as `wiki/_raw/infra/` or `wiki/_raw/projects/<project-name>/`. Preserve the original content.
2. Read `wiki/index.md`, recent `wiki/log.md` entries, and likely related pages.
3. Decide the durable home for the knowledge:
   - `topics/` for concepts and mental models
   - `patterns/` for reusable engineering designs
   - `playbooks/` for repeatable procedures
   - `decisions/` for tradeoff-driven choices
   - `projects/` for project-specific context
   - `comparisons/` for option comparisons
   - `glossary/` for short definitions
4. Update every relevant durable page rather than leaving knowledge only in a source summary.
5. Add cross-links in both directions where useful.
6. Update `wiki/index.md` so its sections mirror the real generated wiki directories. Group links under headings such as `# Maps`, `# Topics`, `# Patterns`, `# Playbooks`, `# Decisions`, `# Projects`, `# Comparisons`, `# Glossary`, and `# Meta`; add subheadings for actual subdirectories such as `## topics/ai-engineering` only when they contain pages. Do not keep a flat topic list when the filesystem is hierarchical.
7. Update `wiki/log.md`. Do not blindly append a new entry for every small correction. Before adding an entry, scan the current date and merge with an existing same-day entry when the action and title are the same or when the new change is part of the same maintenance thread. Revise that entry's `pages` and `notes` instead of creating several near-duplicate same-day entries.

Logs are newest-first and grouped with heading levels:
   - `# YYYY`
   - `## YYYY-MM`
   - `### YYYY-MM-DD | action | Title`

Use this entry shape:

```markdown
### YYYY-MM-DD | ingest | Source title
- raw: `wiki/_raw/infra/source-file.ext`
- pages: `topics/frontend/topic.md`, `patterns/pattern.md`
- notes: one-line summary of what changed
```

If the year or month section does not exist, create it above older sections.

For same-day consolidation, prefer one concise entry like:

```markdown
### YYYY-MM-DD | revise | Agent Skill 基础概念
- raw: `wiki/_raw/ai-engineering/grill-me-web-sources.md`
- pages: `topics/ai-engineering/agent-skills-basic-concepts.md`, `index.md`, `log.md`
- notes: 整理 grill-me 条目：合并到 skill 聚合页、按分类组织、修正可访问来源链接。
```

over several mechanical `revise` entries for each tiny formatting or link fix.

### Answer From The Wiki

1. Read `wiki/index.md` first.
2. Search the wiki with `rg` before reading raw files.
3. Answer from compiled wiki pages when enough evidence exists.
4. Fall back to `wiki/_raw/` only when the wiki lacks coverage or the user asks for source-level verification.
5. Offer to file durable answers under the most specific durable home. Use `comparisons/` for option analysis, `playbooks/` for repeatable procedures, and `patterns/` or `topics/` for reusable engineering knowledge.

### Lint And Maintain

Periodically inspect for:

- orphan pages with no inbound links
- `wiki/index.md` sections that do not match the current filesystem layout
- pages missing frontmatter or source provenance
- duplicated concepts split across multiple pages
- stale claims superseded by newer sources
- contradictions between pages
- raw files whose durable knowledge has not been reflected in the wiki
- same-day `wiki/log.md` entries that should be consolidated
- important concepts, patterns, playbooks, decisions, or projects mentioned repeatedly without their own page

Write lint findings to `meta/lint-report.md`, fix mechanical issues directly, and ask before judgment-heavy rewrites.

### Export

Markdown is already the canonical wiki. To produce a single HTML file, run:

```bash
python3 ~/.agents/skills/sean-llm-wiki/scripts/export_single_html.py wiki --output wiki/exports/wiki.html
```

For the default wiki root, run:

```bash
python3 "$HOME/.agents/skills/sean-llm-wiki/scripts/export_single_html.py" "$HOME/Desktop/demo/sean_raw/wiki" --output "$HOME/Desktop/demo/sean_raw/wiki/exports/wiki.html"
```

If the skill is installed somewhere else, run the script from that actual skill path. After export, insert an `export` entry into `wiki/log.md` using the newest-first year/month/day heading format.

## Resources

- `references/wiki-taxonomy.md`: filing decision tree and visual organization rules.
- `scripts/export_single_html.py`: dependency-free markdown-to-single-HTML exporter for browsing and sharing the wiki.
