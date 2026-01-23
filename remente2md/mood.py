"""Mood assessment conversion logic."""

from pathlib import Path
from typing import Any

from slugify import slugify

from . import lib
from .constants import INPUT_CREATED_AT_KEY, MOOD_ASSESSMENT_TAG, OUTPUT_CREATED_AT_KEY


def _create_mood_metadata(
    datetime_str: str, mood: int | None, feelings: list[str]
) -> dict[str, Any]:
    """Build metadata dictionary for mood assessment frontmatter."""
    slugified_feelings = [slugify(feeling) for feeling in feelings]

    return {
        INPUT_CREATED_AT_KEY: datetime_str,
        "mood": mood,
        "feelings": slugified_feelings,
        "tags": [MOOD_ASSESSMENT_TAG],
    }


def convert_mood_assessments(input_file: str, output_dir: str) -> None:
    """
    Convert Remente mood assessment JSON to individual Markdown files.

    Each assessment becomes a timestamped Markdown file with YAML frontmatter.
    Raises on first error encountered.
    """
    notes = lib.load_notes(input_file)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    processed_count = 0
    for note in notes:
        try:
            date_str, datetime_str = lib.parse_note_date(note[OUTPUT_CREATED_AT_KEY])

            metadata = _create_mood_metadata(
                datetime_str,
                note["rating"],
                note.get("feelings", []),
            )

            lib.write_note(
                output_path, date_str, note.get("notes", ""), frontmatter_data=metadata
            )
            processed_count += 1
        except Exception as e:
            print(f"Error processing note: {e}")
            raise

    print(f"\nSuccessfully processed {processed_count} mood assessment file(s)")
