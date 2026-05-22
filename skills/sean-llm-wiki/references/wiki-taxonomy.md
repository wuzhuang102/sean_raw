# Wiki Taxonomy

Use this taxonomy to keep the wiki useful as a full-stack engineering knowledge base for humans and LLMs.

## Classification Decision Tree

Choose the first matching home:

1. Is this a navigation surface or reading path? Put it in `maps/`.
2. Is this a lightweight record of something the user read or wants to remember by link and summary? Put it in exactly one `reading-notes/<category>/index.md` file.
3. Is this a durable technical concept, method, problem, or mental model? Put it in `topics/`.
4. Is this a reusable engineering design with tradeoffs and failure modes? Put it in `patterns/`.
5. Is this a repeatable debugging, shipping, or operating procedure? Put it in `playbooks/`.
6. Is this a tradeoff-driven technical choice? Put it in `decisions/`.
7. Is this about a concrete project, product, repo, incident, or workstream? Put it in `projects/`.
8. Is this a comparison between technologies, designs, or options? Put it in `comparisons/`.
9. Is this a short definition? Put it in `glossary/`.
10. Is this about maintaining the wiki itself? Put it in `meta/`.

If a page could live in several places, put it where a reader would first look and add cross-links from the other relevant category pages.

## Visual Navigation Rules

- Keep `wiki/index.md` as the table of contents, grouped by semantic directories.
- Maintain one short directory landing page when a section grows past 10 pages, for example `topics/frontend/index.md`.
- Use map pages for dense areas, for example `maps/ai-engineering-map.md` linking to retrieval, evaluation, agents, memory, and prompting.
- Prefer many small focused pages over giant pages when graph navigation matters.
- Prefer synthesis pages when readers need a guided narrative instead of a graph.
- Keep titles human-facing; avoid opaque IDs unless the raw source requires them.

## Link Patterns

- Topic, pattern, playbook, decision, project, and comparison pages should cite raw sources or stable references in a `# Sources` section.
- Map pages should link to the pages a reader or LLM should open first.
- Playbooks should link to the patterns and topics that explain the underlying mechanisms.
- Decisions should link to comparisons, project context, and raw evidence.
- Project pages should link to relevant decisions, playbooks, incidents, and lessons.

## Page Types

`map`: A navigation page for a domain, workflow, or learning path.

`topic`: A concept that remains useful across sources and questions.

`pattern`: A reusable engineering design with tradeoffs and failure modes.

`playbook`: A repeatable operating procedure.

`decision`: An architecture decision record or technical choice.

`project`: A live or archived workstream, repo, product, incident, or implementation context.

`comparison`: A structured comparison between technologies, designs, or options.

`glossary`: A short concept definition.

`reading-note`: A lightweight source record stored in a category `reading-notes/*/index.md` file. It keeps the link, a concise summary, tags, and optional `distilled` references, but does not become a standalone source page by default.

`meta`: Wiki maintenance, taxonomy, lint, contradiction, and export records.
