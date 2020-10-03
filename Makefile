install:
	@poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest --verbose --cov=gendiff  --cov-report xml tests/

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install lint test selfcheck check
