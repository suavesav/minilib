migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations

runserver:
	@poetry run python manage.py runserver

shell:
	@poetry run ptipython --vi
