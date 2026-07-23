"""Build docs/_build/html/llms.txt from the Jupyter Book table of contents."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
OUTPUT_PATH = DOCS_DIR / "_build" / "html" / "llms.txt"


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream) or {}


def iter_toc_files(node: dict[str, Any]) -> list[str]:
    files: list[str] = []

    if "root" in node:
        files.append(node["root"])
    if "file" in node:
        files.append(node["file"])

    for key in ("parts", "chapters", "sections"):
        for child in node.get(key, []) or []:
            files.extend(iter_toc_files(child))

    return files


def resolve_doc_path(doc_name: str) -> Path | None:
    candidate = DOCS_DIR / doc_name
    if candidate.suffix:
        return candidate if candidate.exists() else None

    for suffix in (".md", ".rst", ".ipynb"):
        with_suffix = candidate.with_suffix(suffix)
        if with_suffix.exists():
            return with_suffix

    return None


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def heading_from_markdown(lines: list[str]) -> str | None:
    for line in lines:
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return strip_markup(match.group(1))
    return None


def heading_from_rst(lines: list[str]) -> str | None:
    for index, line in enumerate(lines[:-1]):
        title = line.strip()
        underline = lines[index + 1].strip()
        if title and len(underline) >= len(title) and set(underline) <= set("=-~^\"'`"):
            return strip_markup(title)
    return None


def strip_markup(text: str) -> str:
    text = re.sub(r"`([^`<]+?)\s*<[^`]+>`_", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`{}]", "", text)
    return " ".join(text.split())


def extract_title(path: Path, text: str) -> str:
    lines = text.splitlines()
    title = heading_from_markdown(lines) if path.suffix == ".md" else heading_from_rst(lines)
    return title or path.stem.replace("_", " ").replace("-", " ").title()


def normalize_source_text(path: Path, text: str) -> str:
    if path.suffix == ".ipynb":
        return notebook_to_markdown(text)

    lines = text.splitlines()
    in_front_matter = False
    normalized: list[str] = []

    for index, line in enumerate(lines):
        stripped = line.strip()

        if index == 0 and stripped == "---":
            in_front_matter = True
            continue
        if in_front_matter:
            if stripped == "---":
                in_front_matter = False
            continue

        if re.match(r"^\([^)]+\)=$", stripped):
            continue

        normalized.append(line.rstrip())

    return trim_blank_lines("\n".join(normalized))


def notebook_to_markdown(text: str) -> str:
    notebook = json.loads(text)
    blocks: list[str] = []

    for cell in notebook.get("cells", []):
        source = "".join(cell.get("source", []))
        if not source.strip():
            continue

        cell_type = cell.get("cell_type")
        if cell_type == "markdown":
            blocks.append(trim_blank_lines(source))
        elif cell_type == "code":
            blocks.append("```python\n" + source.rstrip() + "\n```")

    return trim_blank_lines("\n\n".join(blocks))


def trim_blank_lines(text: str) -> str:
    lines = text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def build_llms_txt() -> str:
    config = load_yaml(DOCS_DIR / "_config.yml")
    toc = load_yaml(DOCS_DIR / "_toc.yml")
    title = config.get("title", "Documentation")
    repository = config.get("repository", {})
    repository_url = repository.get("url")

    entries: list[tuple[str, Path, str]] = []
    seen: set[Path] = set()

    for doc_name in iter_toc_files(toc):
        path = resolve_doc_path(doc_name)
        if path is None:
            print(f"warning: docs TOC entry not found: {doc_name}", file=sys.stderr)
            continue
        if path in seen:
            continue
        seen.add(path)

        text = read_text(path)
        entries.append((extract_title(path, text), path, normalize_source_text(path, text)))

    lines = [
        f"# {title}",
        "",
        "> Documentation for the NAWI Water Treatment Ontology.",
        "",
    ]

    if repository_url:
        lines.extend([f"Repository: {repository_url}", ""])

    lines.extend(
        [
            "This file inlines the main documentation pages in reading order for language model agents.",
            "",
            "## Documentation",
        ]
    )

    for entry_title, path, body in entries:
        source = path.relative_to(DOCS_DIR).as_posix()
        lines.extend(
            [
                "",
                f"---",
                "",
                f"## {entry_title}",
                "",
                f"Source: docs/{source}",
                "",
                body,
            ]
        )

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_llms_txt(), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
