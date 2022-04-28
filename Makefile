.DEFAULT_GOAL := help

DOCKER_COMPOSE = $(shell which docker-compose)  -f docker-compose.yml

.PHONY: install
install: ## Install project
	make copy-env
	make start

pull: ## Pull project
	git checkout master && git pull origin master

start: ## Start project
	$(DOCKER_COMPOSE) up

build: ## Build project
	$(DOCKER_COMPOSE) build

copy-env:
	cp -rf .env.local.dist .env
