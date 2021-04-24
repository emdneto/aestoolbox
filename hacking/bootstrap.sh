#!/bin/bash

#sudo apt install build-essential git vim python3.8 python3-pip 

_hacking_dir="$(pwd)/hacking"
source $_hacking_dir/common.sh
find_python

$PYTHON_BIN -m pip install pipenv

if test -f "$PWD/Pipfile"; then
    $PYTHON_BIN -m pipenv install --dev
else
    $PYTHON_BIN -m pipenv install -r $_hacking_dir/requirements_dev.txt --dev
fi

$PYTHON_BIN -m pipenv run pre-commit install