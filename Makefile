build:
	docker-compose build

up:
	docker-compose up web

test_via_nginx:
	docker-compose up -d web
	docker-compose run test pytest -s -v --entry_point=nginx
	docker-compose stop -t 1 web

stop:
	docker-compose stop -t 1 web