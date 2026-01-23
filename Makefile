SHELL = /bin/bash

OUT_DIR = output
SAMPLE_LIFE_PATH = sample/data_life_assessments.json
SAMPLE_MOOD_PATH = sample/data_mood_assessments.json


install:
	poetry install --no-root


help:
	poetry run ... -h

demo:
	poetry run ... life $(SAMPLE_LIFE_PATH)
	poetry run ... mood $(SAMPLE_MOOD_PATH)
