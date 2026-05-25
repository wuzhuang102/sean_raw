---
name: sean-llm-wiki
description: Build and maintain a persistent LLM-written full-stack engineering wiki from raw sources and lightweight catalog entries. Use when the user wants to ingest files, notes, URLs, transcripts, research, conversations, or project context into a structured wiki under wiki/, keep immutable raw inputs outside generated knowledge files when needed, classify lightweight items under overview pages, update markdown knowledge files with provenance and cross-links, lint the knowledge base, answer questions from the wiki, or export the wiki as markdown and a single self-contained HTML file.
disable-model-invocation: true
---

## Operating Model

Treat the wiki as a compiled knowledge layer between raw sources and answers. The target shape is a full-stack engineering knowledge base: useful for human browsing, LLM retrieval, interview preparation, architecture work, debugging, and project memory.

- Keep raw sources immutable under `<project>/wiki/_raw/` when raw capture is needed. Create semantic subdirectories on demand; do not pre-create empty raw categories. Do not use `<project>/raw/` for this skill.
- Maintain generated wiki knowledge files in `<project>/wiki/`.
- Prefer markdown as the canonical format.
- Generate single-file HTML exports only from the markdown wiki; do not edit exported HTML as source.
- Update `wiki/index.md` and `wiki/log.md` on every ingest, reading-note update, query-to-page, lint pass, or export. Keep `wiki/log.md` newest-first, grouped by year and month.
- Cite raw sources and existing wiki knowledge files for non-obvious claims.
- Ask before overwriting user-authored pages or resolving contradictions that require judgment.
- Treat the wiki's own filing rules as persistent state. On every ingest, reading-note update, or durable-page update, read `wiki/_meta/filing-rules.md` when it exists and follow it before the bundled taxonomy. If the user changes filing preferences, update that file so later runs continue the same classification behavior.

Use `$HOME/Desktop/demo/sean_raw` as the default project root. The maintained wiki lives under `$HOME/Desktop/demo/sean_raw/wiki`. Expand `~` or `$HOME` at runtime instead of hard-coding the current username. If the user explicitly points to another root for a specific task, use that root for that task only.

## Directory Model

Do not hard-code or pre-create a full wiki tree. Create only the files and directories required by the current task.

Minimal first-use shape:

- `index.md`: human and LLM navigation.
- `log.md`: newest-first maintenance log.
- `knowledge/`: compiled knowledge files, catalogs, maps, playbooks, comparisons, decisions, and project records.
- `notes/`: lightweight reading records. Create a category file only when it has at least one real entry.
- `_raw/`: internal provenance, created only when raw capture is needed. Create semantic subdirectories on demand.
- `_meta/`: local filing rules, lint reports, contradictions, migrations, and other maintenance state.
- `exports/`: generated outputs, created only when exporting.

Avoid empty placeholder files and empty directories. The directory structure should follow the actual accumulated wiki, not an upfront taxonomy template.

Default filing conventions:

- Use `knowledge/` for durable knowledge regardless of whether the page is a topic, pattern, playbook, decision, project, comparison, glossary entry, or map.
- Use one focused markdown file per durable knowledge entry. Add `type` in frontmatter to preserve the semantic role instead of splitting top-level directories by type.
- Use `notes/<category>.md` for reading notes, and only create category files that contain entries.
- Use `knowledge/<catalog>.md` for lightweight catalogs such as AI tools; classify items inside the parent catalog until an item deserves expansion.
- Use `_meta/filing-rules.md` as the project-local classification source of truth.

For detailed filing rules, read `references/wiki-taxonomy.md`.

## Page Conventions

Use concise YAML frontmatter on generated markdown knowledge files. The readable title is derived from the filename or index entry, so do not add a separate level-1 heading just to repeat the filename. Start the generated body at level-1 headings for real content sections (`# Section`), then use `##`, `###`, and lower levels for subsections. Do not duplicate the filename as a `title` field unless a downstream integration explicitly requires it.

```yaml
---
type: "map|catalog|topic|pattern|playbook|decision|project|comparison|glossary|meta"
status: "draft|active|contested|stale|archived"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
sources:
  - "../_raw/infra/example.md"
tags: []
---
```

Prefer stable, readable filenames: lowercase words separated by hyphens for English, or clear Chinese names when Chinese better matches the material. Keep one major concept per page. Use wiki links or normal relative markdown links consistently with the surrounding wiki. Add a `# Sources` section when a page aggregates claims from multiple raw files.

For user-facing sources, cite links a reader can open directly: official docs, GitHub files/directories, papers, standards, or stable external pages. Do not make the page body say "source: raw" or point readers only to `wiki/_raw/...`; raw files are internal provenance for frontmatter, logs, and maintenance. When using web links, verify important links before writing them, preferably with `curl -I` or an equivalent check, and replace broken or unstable marketplace mirrors with the most direct stable source.

When claims conflict, mark affected pages `status: contested`, add a short `# Contested Claims` section, and log the conflict in `_meta/contradictions.md`. Do not silently choose a winner unless the user gives a rule.

## Filing Rules And Lightweight Entries

Before deciding whether to create a new durable knowledge file, read `wiki/_meta/filing-rules.md` if it exists. Use it as the local source of truth for:

- which kinds of material should become standalone knowledge files
- which kinds should be appended as entries under an existing overview, map, catalog, or category page
- how entries should be classified inside that parent catalog
- when raw source capture is required

Default behavior:

1. Create a standalone durable knowledge file only when the material introduces a reusable concept, pattern, playbook, decision, project, comparison, or glossary term that is likely to be opened independently.
2. Append a lightweight entry to an existing overview/catalog page when the material is mainly a classification, short description, tool listing, link, or early-stage observation.
3. Prefer updating the most relevant parent catalog over creating a new page when the user's wording includes "简单记录", "归类", "加到专栏", "作为子项", "概括", "先别展开", "轻量整理", or similar intent.
4. Inside a parent catalog, classify entries under stable headings defined in `wiki/_meta/filing-rules.md`; create a new heading only when the rules allow it or no existing heading fits.
5. For lightweight entries, include source links directly in the entry. Do not create a separate generated page for the entry unless the user asks to expand it later.
6. Raw capture is required for evidence-heavy durable synthesis, fetched documents, inaccessible/private sources that need provenance, and claims that may be disputed later. Raw capture is optional for lightweight entries that only record a public link, a user-provided summary, or a brief classification.
7. When a lightweight entry is later expanded into a durable knowledge file, keep the parent entry as a short index row and link to the new file.
8. Log lightweight-entry work with action `classify` or `catalog`, and use `raw: none` when no raw file was created.

## Workflows

### Capture Reading Notes

Use this workflow when the user asks to save, file, summarize, or remember an article, book, paper, doc, transcript, video, or link as reading material. This is distinct from durable wiki synthesis.

1. Put the reading record under `notes/`, not under durable knowledge files by default.
2. Use one primary category only. Prefer these categories unless the user gives a stronger local taxonomy:
   - `notes/technology.md`: engineering, AI, architecture, tools, technical papers, and implementation writeups
   - `notes/work.md`: management, collaboration, project retrospectives, organizational process, and career material
   - `notes/product.md`: product design, UX, growth, requirements, and user research
   - `notes/business.md`: companies, industries, commercial models, markets, and strategy
   - `notes/personal.md`: personal growth, learning systems, life systems, and non-work methods
   - `notes/misc.md`: material that does not yet have a stable home
   Create the category file only when adding a real entry.
3. Do not duplicate the same source across multiple category files. Use `tags` for cross-category attributes.
4. Inside each category markdown file, keep entries newest-first by record date, grouped by year and month:

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
9. When the user gives a special instruction such as "沉淀观点", "整理到知识库", "更新相关文档", "归纳成长期知识", "加入 wiki", "整理重要观点", or "提炼到合适文档", first write or update the reading-note entry, then update the most relevant durable wiki knowledge files. Prefer existing pages found through `wiki/index.md` and `rg`; create a new `knowledge/` file only when no suitable page exists.
10. When durable knowledge files are updated from a reading note, add a `distilled` line to the reading-note entry:

```markdown
- distilled: `knowledge/example.md`
```

11. Update `wiki/index.md` so it includes `# Notes` and links directly to existing category markdown files such as `notes/technology.md`. Do not create or link empty note files. Update `wiki/log.md` with action `reading-note`; consolidate same-day reading-note work when it is part of the same thread.

### Capture Lightweight Entries

Use this workflow when the user asks to classify, briefly summarize, add to a column/catalog, keep as a child item, or avoid expanding a source into its own page.

1. Read `wiki/_meta/filing-rules.md` if it exists, then read `wiki/index.md` and the likely parent catalog.
2. Choose the parent catalog from local rules. If no parent catalog exists, create a `knowledge/` catalog only when it represents a reusable catalog; otherwise ask one concise question.
3. Add the item under the closest existing heading. If no heading fits, create the smallest reasonable heading allowed by the local rules.
4. Keep the entry compact and structured. Prefer fields such as `分类`, `定位`, `技术路径`, `适合场景`, `风险`, and `来源` when the parent catalog uses them.
5. Put stable public links directly in the entry. Do not create a raw file unless the source is long, private, likely to disappear, evidence-heavy, or the user explicitly wants raw preservation.
6. Do not create a standalone generated page for the item. If later expansion is needed, keep the original parent entry as a short index row and link to the expanded page.
7. Update `wiki/index.md` only if the parent catalog is new or its description changed.
8. Update `wiki/log.md` with action `classify` or `catalog`; use `raw: none` when no raw file was created.

### Ingest Raw Sources

1. Read `wiki/_meta/filing-rules.md` if it exists, then read `wiki/index.md`, recent `wiki/log.md` entries, and likely related pages.
2. First decide whether the material should be a standalone durable knowledge file, an update to existing durable knowledge files, or a lightweight entry in an existing parent catalog. If it is lightweight, use the `Capture Lightweight Entries` workflow.
3. Put or confirm the raw file under a semantic subdirectory of `wiki/_raw/`, such as `wiki/_raw/infra/` or `wiki/_raw/projects/<project-name>/`, only when raw capture is needed. Preserve the original content.
4. If the material should become durable knowledge, create or update a focused file under `knowledge/`. Use the `type` frontmatter field to mark whether it is a topic, pattern, playbook, decision, project, comparison, glossary entry, map, or catalog.
5. Update every relevant durable knowledge file rather than leaving knowledge only in a source summary.
6. Add cross-links in both directions where useful.
7. Update `wiki/index.md` so it mirrors the real generated wiki, usually with `# Knowledge`, `# Notes`, and `# Maintenance`. Do not list empty categories or directories.
8. Update `wiki/log.md`. Do not blindly append a new entry for every small correction. Before adding an entry, scan the current date and merge with an existing same-day entry when the action and title are the same or when the new change is part of the same maintenance thread. Revise that entry's `knowledge` and `notes` instead of creating several near-duplicate same-day entries.

Logs are newest-first and grouped with heading levels:
   - `# YYYY`
   - `## YYYY-MM`
   - `### YYYY-MM-DD | action | Title`

Use this entry shape:

```markdown
### YYYY-MM-DD | ingest | Source title
- raw: `wiki/_raw/infra/source-file.ext`
- knowledge: `knowledge/topic.md`, `knowledge/pattern.md`
- notes: one-line summary of what changed
```

If the year or month section does not exist, create it above older sections.

For same-day consolidation, prefer one concise entry like:

```markdown
### YYYY-MM-DD | revise | Agent Skill 基础概念
- raw: `wiki/_raw/ai-engineering/grill-me-web-sources.md`
- knowledge: `knowledge/agent-skills-basic-concepts.md`, `index.md`, `log.md`
- notes: 整理 grill-me 条目：合并到 skill 聚合页、按分类组织、修正可访问来源链接。
```

over several mechanical `revise` entries for each tiny formatting or link fix.

### Answer From The Wiki

1. Read `wiki/index.md` first.
2. Search the wiki with `rg` before reading raw files.
3. Answer from compiled wiki knowledge files when enough evidence exists.
4. Fall back to `wiki/_raw/` only when the wiki lacks coverage or the user asks for source-level verification.
5. Offer to file durable answers under `knowledge/`, using frontmatter `type` to distinguish option analysis, repeatable procedures, reusable engineering patterns, topics, projects, and decisions.

### Lint And Maintain

Periodically inspect for:

- orphan knowledge files with no inbound links
- `wiki/index.md` sections that do not match the current filesystem layout
- empty placeholder files or empty directories created without actual content
- knowledge files missing frontmatter or source provenance
- duplicated concepts split across multiple knowledge files
- stale claims superseded by newer sources
- contradictions between pages
- raw files whose durable knowledge has not been reflected in the wiki
- same-day `wiki/log.md` entries that should be consolidated
- important concepts, patterns, playbooks, decisions, or projects mentioned repeatedly without their own knowledge file

Write lint findings to `_meta/lint-report.md`, fix mechanical issues directly, and ask before judgment-heavy rewrites.

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
