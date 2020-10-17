install:
	@poetry install

lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest -v --verbose --cov=gendiff tests/

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install lint test selfcheck check
