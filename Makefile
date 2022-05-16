install:
	pip install poetry
	poetry install
	poetry export -f requirements.txt --output requirements.txt
	pip install -r requirements.txt

test:
	pytest task_manager -vv

test-coverage:
	pytest --cov=task_manager --cov-report xml

test-show:
	pytest --cov=task_manager --cov-report term-missing

lint:
	poetry run flake8 task_manager

check:
	poetry check

build:
	poetry build
	
package-install:
	pip install --user dist/*.whl

deps-export:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: install test lint check build

