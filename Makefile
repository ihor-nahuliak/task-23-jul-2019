.PHONY: clean install test

DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
SHELL=/bin/bash

GLOBAL_PYTHON = /usr/bin/python3.6
ENV := $(DIR)/env/bin
PYTHON := $(ENV)/python
PIP := $(ENV)/pip

STATUS_ERROR := \033[1;31m*\033[0m Error
STATUS_OK := \033[1;32m*\033[0m OK


clean-pyc:
	find . -name '*.pyc' -exec rm -f {} + ;\
	find . -name '*.pyo' -exec rm -f {} + ;\
	find . -name '*~' -exec rm -f {} + ;\
	if [ $$? -eq 0 ]; then \
		echo -e "${STATUS_OK}" ;\
	else \
		echo -e "${STATUS_ERROR}" ;\
	fi;

clean: clean-pyc


install-env-python:
	rm -rf "$(DIR)/env/" ;\
	virtualenv -p $(GLOBAL_PYTHON) --clear "$(DIR)/env/" ;\
	if [ $$? -eq 0 ]; then \
		echo -e "${STATUS_OK}" ;\
	else \
		echo -e "${STATUS_ERROR}" ;\
	fi;

env-activate:
	. $(ENV)/activate

install-python-libs:
	$(PIP) install -U pip ;\
	$(PIP) install --no-cache-dir --upgrade -r "$(DIR)/requirements.txt" ;\
	if [ $$? -eq 0 ]; then \
		echo -e "${STATUS_OK}" ;\
	else \
		echo -e "${STATUS_ERROR}" ;\
	fi;

install: install-env-python env-activate install-python-libs

test-init-migrations:
	@SETTINGS="app.settings.testing" \
	$(PYTHON) $(DIR)/app/migrations/manage.py version_control >>/dev/null 2>&1 ;\
	echo 0

test-migrations:
	SETTINGS="app.settings.testing" \
	$(PYTHON) $(DIR)/app/migrations/manage.py test ;\
	if [ $$? -eq 0 ]; then \
		echo -e "${STATUS_OK}" ;\
	else \
		echo -e "${STATUS_ERROR}" ;\
	fi;

test-upgrade-migrations:
	SETTINGS="app.settings.testing" \
	$(PYTHON) $(DIR)/app/migrations/manage.py upgrade ;\
	if [ $$? -eq 0 ]; then \
		echo -e "${STATUS_OK}" ;\
	else \
		echo -e "${STATUS_ERROR}" ;\
	fi;

test-downgrade-migrations:
	SETTINGS="app.settings.testing" \
	$(PYTHON) $(DIR)/app/migrations/manage.py downgrade 0 ;\
	if [ $$? -eq 0 ]; then \
		echo -e "${STATUS_OK}" ;\
	else \
		echo -e "${STATUS_ERROR}" ;\
	fi;

test-python-code:
	SETTINGS="app.settings.testing" \
	$(DIR)/env/bin/py.test \
	-v \
	-q --flakes \
	--cov-config=.coveragerc \
	--cov=app \
	--cov-report=html \
	--doctest-modules \
	tests

test: test-init-migrations test-migrations test-upgrade-migrations test-python-code test-downgrade-migrations
