install:
	poetry install

test:
	pytest task_manager -vv

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml

lint:
	poetry run flake8 task_manager

selfcheck:
	poetry check

check: selfcheck test-coverage lint

build:
	poetry build
	
package-install:
	pip install --user dist/*.whl

deps-export:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: install test lint selfcheck check build

