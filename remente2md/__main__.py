#!/usr/bin/env python3
"""Convert Remente JSON notes to Obsidian markdown files."""

import argparse

from . import life
from . import mood


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Convert Remente JSON assessments to Markdown files."
    )
    parser.add_argument(
        "type",
        choices=["life", "mood"],
        help="Type of assessment to convert (life or mood)",
    )
    parser.add_argument("input", metavar="INPUT_PATH", help="Path to input JSON file")
    parser.add_argument(
        "output", metavar="OUTPUT_PATH", help="Path to output directory"
    )

    args = parser.parse_args()

    if args.type == "life":
        life.convert_life_assessments(args.input, args.output)
    elif args.type == "mood":
        mood.convert_mood_assessments(args.input, args.output)


if __name__ == "__main__":
    main()
