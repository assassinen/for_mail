build:
	docker-compose build

up:
	docker-compose up web

test:
	docker-compose run web pytest tests/

stop:
	docker-compose stop -t 3 web
