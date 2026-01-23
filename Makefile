SHELL = /bin/bash

APP_DIR = remente2md

OUT_DIR = output
OUT_LIFE_PATH = $(OUT_DIR)/life_assessments
OUT_MOOD_PATH = $(OUT_DIR)/mood_assessments

INPUT_DIR = sample
LIFE_PATH = $(INPUT_DIR)/data_life_assessments.json
MOOD_PATH = $(INPUT_DIR)/data_mood_assessments.json


h help:
	@grep '^[a-z]' Makefile


install:
	poetry install --no-root

update:
	poetry update

g install-global:
	pipx install . --force


app-help:
	poetry run python -m $(APP_DIR) -h

demo:
	poetry run python -m $(APP_DIR) life $(LIFE_PATH) $(OUT_LIFE_PATH)
	poetry run python -m $(APP_DIR) mood $(MOOD_PATH) $(OUT_MOOD_PATH)
