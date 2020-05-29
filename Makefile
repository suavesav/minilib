migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations

runserver:
	@poetry run python manage.py runserver

oakshell:
	poetry run python manage.py shell

shell:
	@poetry run ptipython --vi

sqlite:
	sqlite3 db.sqlite3
