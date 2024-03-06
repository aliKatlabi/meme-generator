# Makefile for Python project

# Define the Python interpreter (change this if needed)
PYTHON := python3

# Directories
SRC_DIR := src
ENV_DIR := env

# Files to exclude from linting
EXCLUDE_FILES := $(wildcard $(SRC_DIR)/env/*.py)

# Linting targets
lint:
	@echo "Running pycodestyle and pydocstyle..."
	@$(PYTHON) -m pycodestyle --statistics $(SRC_DIR)/*.py
	@$(PYTHON) -m pydocstyle $(SRC_DIR)/*.py

# Run the server
run:
	@echo "Starting the server..."
	@$(PYTHON) app.py

# MemeGenerator help
meme:
	@echo "Usage: $(PYTHON) meme.py MemeGenerator -h"

.PHONY: lint run meme
