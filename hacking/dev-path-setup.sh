#!/bin/bash
# env variables and find_python function
_hacking_dir="$(pwd)/hacking"
source $_hacking_dir/common.sh
find_python



# Install dev dependencies
if test -f "$PWD/hacking/requirements_dev.txt"; then
    pip install -r $_hacking_dir/requirements_dev.txt


# Setup automatic black formatting, flake8 and commitizen using pre-commit
$PYTHON_BIN -m pipenv run pre-commit install
