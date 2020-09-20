install:
	@poetry install

lint:
	poetry run flake8 gendiff

check:
	poetry run pytest python-project-lvl2 tests

.PHONY: install lint check