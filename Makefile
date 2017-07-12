.PHONY: build run default shell

# Docker container tag
IMAGE_NAME = modularitycontainers/nginx

# An absolute path to your web root
#DOCUMENT_ROOT = /

# A port you want your nginx server to run on host
PORT = 8080

default: run

build:
	docker build --tag=$(IMAGE_NAME) .

run: build
ifdef DOCUMENT_ROOT
	docker run -p $(PORT):80 -v $(DOCUMENT_ROOT):/var/www/html/ $(IMAGE_NAME)
endif

shell:
	docker run -it $(IMAGE_NAME) bash

test:
	cd tests; MODULE=docker MODULEMD=$(MODULEMDURL) URL="docker=$(IMAGE_NAME)" make all
