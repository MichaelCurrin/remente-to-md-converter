# Remente to Markdown converter
> Convert Remente JSON exports of life and mood assessments to Markdown files (Python CLI tool)

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/remente-to-md-converter?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/remente-to-md-converter/releases/)
[![Go to Python website](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMichaelCurrin%2Fremente-to-md-converter%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=project.requires-python&label=python&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)


Export your life and mood assessments from [Remente](https://app.remente.com/) as JSON files and then run this tool to convert them to Markdown files with content and frontmatter.

The use case in mind is for storing the data in an Obsidian vault.

_Note that import CSV is note supported because as of Jan 2025 the CSV exports come out empty._


## Sample usage

```sh
# Convert life assessments
python -m remente2md life exported_data_life_assessments.json life_assessments

# Convert mood assessments
python -m remente2md mood exported_data_mood_assessments.json mood_assessments
```

## Sample output

### Life assessment

Given input: [sample/data_life_assessments.json](sample/data_life_assessments.json).

Result:

```yaml
---
created_at: 2019-02-27 19:44
ratings:
  career-education: 6
  family: 5
  finances: 4
  friends-social-life: 3
  fun-recreation: 1
  health-fitness: 3
  love-relationships: 1
  personal-development: 9
tags:
- remente-life-assessment
---
```

### Mood assessment

Given input: [sample/data_mood_assessments.json](sample/data_mood_assessments.json).

Result:

```yaml
---
created_at: 2019-02-27 19:46
feelings:
- confused
- stressed
- unhappy
- worried
mood: 2
tags:
- remente-mood-assessment
---

My note
```


## Features

- Converts Remente JSON exports to individual Markdown files (one per assessment date)
- Adds YAML frontmatter with metadata for Obsidian integration
- Slugifies rating and feeling keys for consistency (e.g., "Career & Education" → `career-education`)
- Separate handling for life assessments (with ratings) and mood assessments (with mood and feelings)
- Timestamped filenames for easy chronological organization



## Installation

Install Python.

Install Poetry.

Install with pip.

```sh
$ pip install git+https://github.com/MichaelCurrin/rememte-to-md-converter
```

```sh
remente2md --help
```

## Usage

### Basic command

```bash
remente2md TYPE INPUT_PATH OUTPUT_PATH
```


## Development

Clone the repository and install dependencies using Poetry:

```bash
git clone https://github.com/MichaelCurrin/remente-to-md-converter.git
cd remente-to-md-converter
make install
```

```bash
poetry run python -m remente2md TYPE INPUT_PATH OUTPUT_PATH
```

Show available commands:

```bash
make help
```

Test using the demo:

```sh
make demo
```


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
