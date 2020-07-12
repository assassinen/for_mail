build:
	docker-compose build

up:
	docker-compose up web

test:
	docker-compose up -d web
	docker-compose run test pytest -s -v
	docker-compose stop -t 1 web

stop:
	docker-compose stop -t 1 web
