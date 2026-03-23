# Remente to Markdown converter
> Convert Remente JSON exports of life and mood assessments to Markdown files (Python CLI tool)

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/remente-to-md-converter?include_prereleases=&sort=semver&color=blue)](https://github.com/MichaelCurrin/remente-to-md-converter/releases/)
[![Go to Python website](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMichaelCurrin%2Fremente-to-md-converter%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=project.requires-python&label=python&logo=python&logoColor=white)](https://python.org)
[![OS - Linux](https://img.shields.io/badge/OS-Linux-blue?logo=linux&logoColor=white)](https://www.linux.org/ "Go to Linux homepage")
[![OS - macOS](https://img.shields.io/badge/OS-macOS-blue?logo=apple&logoColor=white)](https://www.apple.com/macos/ "Go to Apple homepage")
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)


Export your life and mood assessments from [Remente](https://app.remente.com/) as JSON files and then run this tool to convert them to Markdown files with content and frontmatter.

The use case in mind here is for storing the data in an Obsidian vault.

_Note that importing a CSV is not supported because as of January 2025 the Remente CSV exports come out empty._


## Sample usage

Convert life assessments:

```sh
remente2md life exported-life.json output/life_assessments
```

Convert mood assessments:

```sh
remente2md mood exported-mood.json output/mood_assessments
```

## Sample output

### Life assessment

Given input: [sample/data_life_assessments.json](/sample/data_life_assessments.json).

Result:

- `output/life/2019-02-27.md`
    ```yaml
    ---
    career_education: 6
    created_at: 2019-02-27T19:44
    family: 5
    finances: 4
    friends_social_life: 3
    fun_recreation: 1
    health_fitness: 3
    love_relationships: 1
    personal_development: 9
    tags:
    - remente-life-assessment
    ---
    ```

### Mood assessment

Given input: [sample/data_mood_assessments.json](/sample/data_mood_assessments.json).

Result:

- `output/life/2019-02-27.md`
    ```yaml
    ---
    created_at: 2019-02-27T19:46
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

- Converts Remente JSON exports to individual Markdown files (one per assessment date).
- Adds YAML frontmatter with metadata for Obsidian integration.
- Slugifies rating and feeling keys for consistency (e.g. "Career & Education" → `career_education`)
- Separate handling for life assessments (with ratings) and mood assessments (with mood and feelings).
- Timestamped filenames for easy chronological organization.


## Setup and run

Install Python.

Install with pip:

```sh
$ pip install git+https://github.com/MichaelCurrin/remente-to-md-converter
```

## Usage

```sh
remente2md --help
```

```sh
remente2md {life,mood} INPUT_PATH OUTPUT_PATH
```

The recommended flow is to:

1. Install `remente2md` globally using the steps above.
1. Make a directory.
1. Create this script in the directory. e.g. `convert.sh`
    ```sh
    LIFE_PATH='data_life_assessments.json'
    MOOD_PATH='data_mood_assessments.json'

    remente2md life "$LIFE_PATH" 'output/life'
    remente2md mood "$MOOD_PATH" 'output/mood'
    ```
1. Download your Remente JSON files to the directory. Rename them to match the names in the script.
1. Run the script.
    ```sh
    bash convert.sh
    ```
1. Review your output files in the created `output` directory.

## Development

Clone the repository and install dependencies using Poetry:

```bash
git clone https://github.com/MichaelCurrin/remente-to-md-converter.git
cd remente-to-md-converter
make install
```

```sh
poetry run python -m remente2md TYPE INPUT_PATH OUTPUT_PATH
```

Show available commands:

```sh
make help
```

Test using the demo:

```sh
make demo
```


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
