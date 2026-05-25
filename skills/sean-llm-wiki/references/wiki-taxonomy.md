# Wiki Taxonomy

Use this taxonomy to keep the wiki useful as a full-stack engineering knowledge base for humans and LLMs.

The filesystem stays intentionally small. Semantic distinctions live in frontmatter and page structure, not in many top-level directories.

## Directory Model

- `knowledge/`: durable knowledge files, maps, catalogs, patterns, playbooks, decisions, projects, comparisons, and glossary-like entries.
- `notes/`: lightweight reading records, one category file only when the category has real entries.
- `_raw/`: immutable source captures, created only when provenance is needed.
- `_meta/`: local filing rules, lint reports, contradictions, migrations, and maintenance notes.
- `exports/`: generated outputs, created only when exporting.

Do not pre-create empty directories or placeholder category files.

## Classification Decision Tree

Choose the first matching handling:

1. Is this about maintaining the wiki itself? Put it in `_meta/`, usually `_meta/filing-rules.md`, `_meta/lint-report.md`, or `_meta/contradictions.md`.
2. Is this a lightweight record of something the user read or wants to remember by link and summary? Put it in exactly one `notes/<category>.md` file.
3. Is this a tool, resource, company, project, link, or short observation that mainly needs classification? Add it as a child entry in the most relevant `knowledge/<catalog>.md`.
4. Is this a navigation surface or reading path? Put it in a focused `knowledge/` file with `type: "map"`.
5. Is this a durable technical concept, method, problem, or mental model? Put it in `knowledge/` with `type: "topic"`.
6. Is this a reusable engineering design with tradeoffs and failure modes? Put it in `knowledge/` with `type: "pattern"`.
7. Is this a repeatable debugging, shipping, or operating procedure? Put it in `knowledge/` with `type: "playbook"`.
8. Is this a tradeoff-driven technical choice? Put it in `knowledge/` with `type: "decision"`.
9. Is this about a concrete project, product, repo, incident, or workstream? Put it in `knowledge/` with `type: "project"`.
10. Is this a comparison between technologies, designs, or options? Put it in `knowledge/` with `type: "comparison"`.
11. Is this a short definition? Prefer a glossary section inside a related page; create a `knowledge/` file with `type: "glossary"` only when the term deserves independent retrieval.

If a page could serve several roles, put it where a reader would first look, set the closest `type`, and add cross-links from other relevant pages.

## Visual Navigation Rules

- Keep `wiki/index.md` as the table of contents, usually grouped as `# Knowledge`, `# Notes`, and `# Maintenance`.
- Link only to files that exist and contain real content.
- Maintain a catalog when a domain has many lightweight child entries, for example `knowledge/ai/summaries/ai-tools.md`.
- Prefer many small focused knowledge files over giant files when graph navigation matters.
- Prefer synthesis files when readers need a guided narrative instead of a graph.
- Keep titles human-facing; avoid opaque IDs unless the raw source requires them.

## Link Patterns

- Durable knowledge files should cite raw sources or stable references in a `# Sources` section.
- Catalogs should link to expanded files when a child item grows beyond a lightweight entry.
- Maps should link to the files a reader or LLM should open first.
- Playbooks should link to the patterns and topics that explain the underlying mechanisms.
- Decisions should link to comparisons, project context, and raw evidence.
- Project records should link to relevant decisions, playbooks, incidents, and lessons.

## Page Types

`map`: A navigation page for a domain, workflow, or learning path.

`catalog`: A parent catalog that holds lightweight classified child entries.

`topic`: A concept that remains useful across sources and questions.

`pattern`: A reusable engineering design with tradeoffs and failure modes.

`playbook`: A repeatable operating procedure.

`decision`: An architecture decision record or technical choice.

`project`: A live or archived workstream, repo, product, incident, or implementation context.

`comparison`: A structured comparison between technologies, designs, or options.

`glossary`: A short concept definition.

`reading-note`: A lightweight source record stored in a category `notes/<category>.md` file. It keeps the link, a concise summary, tags, and optional `distilled` references, but does not become a standalone source page by default.

`meta`: Wiki maintenance, taxonomy, lint, contradiction, and export records.
