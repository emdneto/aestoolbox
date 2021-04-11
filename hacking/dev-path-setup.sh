#!/bin/bash
_hacking_dir="$(pwd)/hacking"

# Install dev dependencies
if test -f "$PWD/hacking/requirements_dev.txt"; then
    pip install -r $_hacking_dir/requirements_dev.txt


# Setup automatic black formatting, flake8 and commitizen using pre-commit
$PYTHON_BIN pre-commit install
