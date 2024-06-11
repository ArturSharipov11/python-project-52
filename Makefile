PORT ?= 8000
WEB_CONCURRENCY ?= 4

install:
	poetry install

dev:
	poetry run python manage.py runserver

compile:
	cd task_manager && poetry run django-admin makemessages -l ru && poetry run django-admin compilemessages --ignore=venv

shell:
	poetry run python manage.py shell

migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate

collectstatic:
	poetry run python manage.py collectstatic
	
start:
	poetry run gunicorn -w $(WEB_CONCURRENCY) -b 0.0.0.0:$(PORT) task_manager.wsgi:application

tests:
	poetry run python3 manage.py test task_manager.tests

coverage:
	poetry run coverage run --source='task_manager' manage.py test task_manager.tests && poetry run coverage xml

lint:
	poetry run flake8 task_manager