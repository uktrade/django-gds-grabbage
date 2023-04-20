build-package:
	poetry build

push-pypi-test:
	poetry publish -r test-pypi

push-pypi:
	poetry publish

serve-docs:
	poetry run mkdocs serve -f ./docs/mkdocs.yml -a localhost:8001

init-example-project:
	poetry run python example_project/manage.py migrate
	poetry run python example_project/manage.py loaddata test_users.json

run-example-project:
	poetry run python example_project/manage.py runserver
