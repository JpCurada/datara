.PHONY: build run cli

PROFILE=johnpaulcurada
PROJECT=datara
TAG=${PROFILE}/${PROJECT}

build:
	docker build -t $(TAG):latest .

run: build
	docker compose up --remove-orphans  #docker run --rm -it -p 8000:8000/tcp $(TAG):$(VER)

dev: build
	docker compose -f docker-compose-dev.yml up --remove-orphans  #docker run --rm -it -p 8000:8000/tcp $(TAG):$(VER)

cli: build
	docker compose run --remove-orphans web sh  #docker run --rm -it -v $$(pwd)/volume:/volume $(TAG):($VER) bash

clean:
	docker system prune -af

test: build
	docker compose run web python manage.py test apps
