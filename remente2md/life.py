"""Life assessment conversion logic."""

from pathlib import Path
from typing import Any

from slugify import slugify

from . import lib
from .constants import (
    MD_CREATED_AT_KEY,
    LIFE_ASSESSMENT_TAG,
    REMENTE_CREATED_AT_KEY,
    SLUGIFY_REPLACEMENTS,
)


def _create_life_metadata(datetime_str: str, ratings: dict[str, int]) -> dict[str, Any]:
    """Build metadata dictionary for life assessment frontmatter."""
    slugified_ratings = {
        slugify(key, replacements=SLUGIFY_REPLACEMENTS): value
        for key, value in ratings.items()
    }
    return {
        MD_CREATED_AT_KEY: datetime_str,
        **slugified_ratings,
        "tags": [LIFE_ASSESSMENT_TAG],
    }


def convert_life_assessments(input_file: str, output_dir: str) -> None:
    """
    Convert Remente life assessment JSON to individual Markdown files.

    Each assessment becomes a timestamped Markdown file with YAML frontmatter.
    Raises on first error encountered.
    """
    notes = lib.load_notes(input_file)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    processed_count = 0
    for note in notes:
        try:
            date_str, datetime_str = lib.parse_note_date(note[REMENTE_CREATED_AT_KEY])

            metadata = _create_life_metadata(
                datetime_str,
                note["ratings"],
            )

            lib.write_note(output_path, date_str, content="", frontmatter_data=metadata)
            processed_count += 1
        except Exception as e:
            print(f"Error processing note: {e}")
            raise

    print(f"\nCompleted life assessments: {processed_count}")
