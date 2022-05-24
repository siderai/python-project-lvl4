install:
	pip install poetry
	pip install --upgrade poetry
	poetry install -v

test:
	poetry run pytest task_manager -vv -s

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml

test-missing:
	poetry run pytest --cov=task_manager --cov-report term-missing

lint:
	poetry run flake8 task_manager

check:
	poetry check

build:
	poetry build
	
package-install:
	make build
	pip install --user dist/*.whl

setup-and-runserver:
	python3 -m venv venv
	source venv/bin/activate
	make install
	python3 manage.py migrate
	make test
	python3 manage.py runserver

deps-export:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: install test lint check build

