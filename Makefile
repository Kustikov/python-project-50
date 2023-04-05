install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 gendiff

make formate:
	poetry run black gendiff

make test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml