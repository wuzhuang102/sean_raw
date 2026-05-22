#!/usr/bin/env python3
"""Export a markdown wiki directory to one self-contained HTML file."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


SKIP_DIRS = {"_raw", "raw", ".git", "node_modules", "__pycache__"}


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :].lstrip()
    return text


def slug(path: Path) -> str:
    raw = str(path.with_suffix("")).replace("/", "-").replace(" ", "-")
    return re.sub(r"[^a-zA-Z0-9_-]+", "-", raw).strip("-").lower()


def inline_md(text: str, link_map: dict[str, str]) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)

    def repl_link(match: re.Match[str]) -> str:
        label = match.group(1)
        target = html.unescape(match.group(2))
        anchor = link_map.get(target) or link_map.get(target.lstrip("./"))
        href = f"#{anchor}" if anchor else target
        return f'<a href="{html.escape(href)}">{label}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl_link, escaped)


def render_markdown(text: str, link_map: dict[str, str]) -> str:
    lines = strip_frontmatter(text).splitlines()
    out: list[str] = []
    in_code = False
    in_ul = False
    in_ol = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    for line in lines:
        if line.startswith("```"):
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                close_lists()
                out.append("<pre><code>")
                in_code = True
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        if not line.strip():
            close_lists()
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            close_lists()
            level = len(heading.group(1))
            body = inline_md(heading.group(2), link_map)
            out.append(f"<h{level}>{body}</h{level}>")
            continue
        ul = re.match(r"^\s*[-*]\s+(.+)$", line)
        if ul:
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(ul.group(1), link_map)}</li>")
            continue
        ol = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if ol:
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(ol.group(1), link_map)}</li>")
            continue
        close_lists()
        out.append(f"<p>{inline_md(line, link_map)}</p>")
    close_lists()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def iter_pages(root: Path) -> list[Path]:
    pages = []
    for path in sorted(root.rglob("*.md")):
        rel_parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        if rel_parts[0] in {"80-exports", "exports"}:
            continue
        pages.append(path)
    return pages


def title_for(path: Path, root: Path) -> str:
    return path.relative_to(root).with_suffix("").as_posix()


def build_html(root: Path) -> str:
    pages = iter_pages(root)
    link_map = {}
    for page in pages:
        rel = page.relative_to(root).as_posix()
        anchor = slug(page.relative_to(root))
        link_map[rel] = anchor
        link_map[f"./{rel}"] = anchor
        link_map[page.name] = anchor

    nav = []
    sections = []
    for page in pages:
        rel = page.relative_to(root)
        anchor = slug(rel)
        title = title_for(page, root)
        nav.append(f'<li><a href="#{anchor}">{html.escape(str(rel))}</a></li>')
        body = render_markdown(page.read_text(encoding="utf-8", errors="replace"), link_map)
        sections.append(
            f'<article id="{anchor}">\n<header><div class="path">{html.escape(str(rel))}</div>'
            f"<h1>{html.escape(title)}</h1></header>\n{body}\n</article>"
        )

    css = """
body{margin:0;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#222;background:#fafafa}
.layout{display:grid;grid-template-columns:minmax(220px,320px) 1fr;min-height:100vh}
nav{position:sticky;top:0;height:100vh;overflow:auto;padding:24px;background:#111;color:#eee}
nav h1{font-size:18px;margin:0 0 16px}
nav ul{list-style:none;padding:0;margin:0}
nav li{margin:0 0 8px;word-break:break-word}
nav a{color:#d7e7ff;text-decoration:none}
main{max-width:920px;padding:32px 48px}
article{padding:28px 0 44px;border-bottom:1px solid #ddd}
article h1{font-size:28px;line-height:1.2;margin:0 0 16px}
article h2{margin-top:28px}
.path{font-size:13px;color:#777;margin-bottom:8px}
pre{overflow:auto;background:#f0f0f0;padding:14px;border-radius:6px}
code{background:#eee;padding:1px 4px;border-radius:4px}
a{color:#0757a8}
@media (max-width:800px){.layout{display:block}nav{position:relative;height:auto}main{padding:24px}}
"""
    return (
        "<!doctype html><html><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        f"<title>{html.escape(root.name)} wiki</title><style>{css}</style></head>"
        "<body><div class=\"layout\"><nav><h1>Wiki</h1><ul>"
        + "\n".join(nav)
        + "</ul></nav><main>"
        + "\n".join(sections)
        + "</main></div></body></html>"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wiki", type=Path, help="Path to the wiki directory")
    parser.add_argument("--output", type=Path, default=None, help="Output HTML path")
    args = parser.parse_args()

    root = args.wiki.resolve()
    if not root.is_dir():
        raise SystemExit(f"Wiki directory not found: {root}")
    output = args.output or root / "exports" / "wiki.html"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_html(root), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
