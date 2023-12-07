
venv:
	python3 -m venv venv

activate:
	source venv/bin/activate

build: requirements.txt
	pip3 install -r requirements.txt
	@touch build

run:
	python3 manage.py runserver

migratefile:
	python3 manage.py makemigrations

migrate:
	python manage.py migrate