build-package:
	poetry build

push-pypi-test:
	poetry publish -r test-pypi

push-pypi:
	poetry publish

serve-docs:
	poetry run mkdocs serve

generate-components:
	poetry run python scripts/generate_components.py

example-project:
	poetry run python example_project/manage.py runserver
