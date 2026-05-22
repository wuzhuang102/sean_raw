---
name: sean-llm-wiki
description: Build and maintain a persistent LLM-written full-stack engineering wiki from raw sources. Use when the user wants to ingest files, notes, URLs, transcripts, research, conversations, or project context into a structured wiki under wiki/, keep immutable raw inputs outside generated pages, update markdown pages with provenance and cross-links, lint the knowledge base, answer questions from the wiki, or export the wiki as markdown and a single self-contained HTML file.
---

## Operating Model

Treat the wiki as a compiled knowledge layer between raw sources and answers. The target shape is a full-stack engineering knowledge base: useful for human browsing, LLM retrieval, interview preparation, architecture work, debugging, and project memory.

- Keep raw sources immutable under `<project>/wiki/_raw/`, grouped into semantic subdirectories such as `frontend/`, `backend/`, `infra/`, `ai-engineering/`, `projects/`, or `sources/`. Do not use `<project>/raw/` for this skill.
- Maintain generated wiki pages in `<project>/wiki/`.
- Prefer markdown as the canonical format.
- Generate single-file HTML exports only from the markdown wiki; do not edit exported HTML as source.
- Update `wiki/index.md` and `wiki/log.md` on every ingest, query-to-page, lint pass, or export. Keep `wiki/log.md` newest-first, grouped by year and month.
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
- `exports/`: generated outputs such as `wiki.html`, PDF-ready markdown, or slide markdown.
- `meta/`: wiki maintenance notes, taxonomy decisions, lint reports, unresolved contradictions.

For detailed filing rules, read `references/wiki-taxonomy.md`.

## Page Conventions

Use concise YAML frontmatter on generated markdown pages. Do not add a standalone level-1 heading as the page title; the readable page title lives in the filename. Start the body directly with the useful content, normally at `##` or lower. Do not duplicate the filename as a `title` field unless a downstream integration explicitly requires it.

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

Prefer stable, readable filenames: lowercase words separated by hyphens for English, or clear Chinese names when Chinese better matches the material. Keep one major concept per page. Use wiki links or normal relative markdown links consistently with the surrounding wiki. Add a `## Sources` section when a page aggregates claims from multiple raw files.

When claims conflict, mark affected pages `status: contested`, add a short `## Contested Claims` section, and log the conflict in `meta/contradictions.md`. Do not silently choose a winner unless the user gives a rule.

## Workflows

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
6. Update `wiki/index.md`.
7. Insert a parseable log entry at the top of the matching month. Logs are newest-first and grouped with heading levels:
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

### Answer From The Wiki

1. Read `wiki/index.md` first.
2. Search the wiki with `rg` before reading raw files.
3. Answer from compiled wiki pages when enough evidence exists.
4. Fall back to `wiki/_raw/` only when the wiki lacks coverage or the user asks for source-level verification.
5. Offer to file durable answers under the most specific durable home. Use `comparisons/` for option analysis, `playbooks/` for repeatable procedures, and `patterns/` or `topics/` for reusable engineering knowledge.

### Lint And Maintain

Periodically inspect for:

- orphan pages with no inbound links
- pages missing frontmatter or source provenance
- duplicated concepts split across multiple pages
- stale claims superseded by newer sources
- contradictions between pages
- raw files whose durable knowledge has not been reflected in the wiki
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
