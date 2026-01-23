#!/usr/bin/env python3
"""Convert Remente JSON notes to Obsidian markdown files."""

import argparse
import json
from pathlib import Path
from datetime import datetime
from typing import Any

import frontmatter


def load_notes(input_file: str) -> list[dict[str, Any]]:
    """Load notes from JSON file."""
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
    date_str = date_obj.strftime("%Y-%m-%d")
    datetime_str = date_obj.strftime("%Y-%m-%d %H:%M")
    return date_str, datetime_str


def create_metadata(
    datetime_str: str, mood: int | None, feelings: list[str]
) -> dict[str, Any]:
    """
    Build metadata dictionary for frontmatter.

    Centralizes metadata structure so it's easy to add/modify fields.
    """
    return {
        "created_at": datetime_str,
        "mood": mood,
        "feelings": feelings,
        "tags": ["remente-mood-assessment"],
    }


def write_note(
    output_path: Path,
    date_str: str,
    note_content: str,
    metadata: dict[str, Any],
) -> None:
    """Write a single note to markdown file with frontmatter."""
    doc = frontmatter.Post(note_content, **metadata)

    output_file = output_path / f"{date_str}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(doc))

    print(f"Created: {output_file}")


def convert_notes(input_file: str, output_dir: str) -> None:
    """
    Convert Remente JSON notes to individual Obsidian markdown files.

    Each note becomes a timestamped markdown file with YAML frontmatter.
    Raises on first error encountered.
    """
    notes = load_notes(input_file)

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    processed_count = 0
    for note in notes:
        try:
            date_str, datetime_str = parse_note_date(note["createdAt"])

            metadata = create_metadata(
                datetime_str,
                note["rating"],
                note.get("feelings", []),
            )

            write_note(output_path, date_str, note.get("notes", ""), metadata)
            processed_count += 1
        except Exception as e:
            print(f"Error processing note: {e}")
            raise

    print(f"\nSuccessfully processed {processed_count} file(s)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Remente JSON notes to Obsidian markdown files."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default="sample/input.json",
        help="Path to input JSON file (default: sample/input.json)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="output",
        help="Path to output directory (default: output)",
    )

    args = parser.parse_args()
    convert_notes(args.input, args.output)
