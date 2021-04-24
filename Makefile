.PHONY: clean clean-test clean-pyc clean-build docs help hacking
.DEFAULT_GOAL := help

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test 

clean-build: 
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -rf {} +

clean-pyc: 
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: 
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with pylint
	flake8 --max-line-length=100 \
			--max-complexity=22 \
			--select=B,C,E,F,W,T4,B9 \
			--exclude=const.py  \
			--extend-exclude=docs/* \
			--extend-exclude=tests/* \
			--ignore=W503,E226,E227,E203 aestoolbox/core

test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source aestoolbox -m pytest
	coverage report -m

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/aestoolbox.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ aestoolbox
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

hacking: 
	$(info *** [DEV] Running ./hacking/run_dev.sh)
	./hacking/bootstrap.sh
