PYTHON=python3

ENVBIN=venv/bin
PIP=$(ENVBIN)/python -m pip
PYTEST=$(ENVBIN)/py.test
FLAKE=$(ENVBIN)/flake8

.PHONY: help clean delpyc install install-dev flake8 tests

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install              -- to initialize virtual environment and requirements"
	@echo "  install-dev          -- to initialize virtual environment, dev tools and requirements"

	@echo "  tests                -- to launch tests using py.test against template hooks"
	@echo "  flake8               -- to proceed to Flake8 checks"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc
	rm -Rf venv

venv:
	$(PYTHON) -m venv venv

install: venv
	$(PIP) install -r requirements/base.txt

install-dev: venv
	$(PIP) install -r requirements/dev.txt

tests:
	$(PYTEST) -vv tests/

flake8:
	@$(FLAKE) \{\{cookiecutter.package_name\}\}
	@$(FLAKE) hooks
