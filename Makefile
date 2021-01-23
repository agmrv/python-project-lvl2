install:
	@poetry install

lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest -v --verbose --cov=gendiff tests/

selfcheck:
	poetry check

check: selfcheck lint test

build: check
	poetry build

publish: build
	poetry publish -r test_pypi

.PHONY: install lint test selfcheck check build publish
