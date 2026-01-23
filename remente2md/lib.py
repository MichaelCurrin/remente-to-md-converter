"""I/O utilities for reading and writing notes."""

import json
from pathlib import Path
from datetime import datetime
from typing import Any

import frontmatter


def load_notes(input_file: str) -> list[dict[str, Any]]:
    """Load notes from a JSON file."""
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"{input_file} not found")

    with open(input_path, encoding="utf-8") as f:
        return json.load(f)


def parse_note_date(created_at: str) -> tuple[str, str]:
    """
    Parse ISO timestamp into date and datetime strings.

    Returns tuple of (date_str for filename, datetime_str for metadata).
    """
    date_obj = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    date_str = date_obj.strftime(r"%Y-%m-%d")
    datetime_str = date_obj.strftime(r"%Y-%m-%d %H:%M")

    return date_str, datetime_str


def write_note(
    output_path: Path,
    date_str: str,
    content: str,
    frontmatter_data: dict[str, Any],
) -> None:
    """Write a single note with frontmatter to a Markdown file."""
    page = frontmatter.Post(content, **frontmatter_data)

    output_file = output_path / f"{date_str}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(page))

    print(f"Created: {output_file}")
