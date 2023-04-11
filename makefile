build-package:
	poetry build

push-pypi-test:
	poetry publish -r test-pypi

push-pypi:
	poetry publish

serve-docs:
	poetry run mkdocs serve -a localhost:8001

generate-components:
	poetry run python scripts/generate_components.py
	poetry run isort --remove-redundant-aliase django_gds_grabbage/gds_components/govuk_frontend
	poetry run autoflake --in-place --remove-unused-variables -r django_gds_grabbage/gds_components/govuk_frontend
	poetry run black django_gds_grabbage/gds_components/govuk_frontend

clear-generated-components:
	find django_gds_grabbage/gds_components/govuk_frontend ! -name '__init__.py' ! -name 'base.py' -type f -exec rm -rf {} +

example-project:
	poetry run python example_project/manage.py runserver
