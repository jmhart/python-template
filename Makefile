APP_NAME := python-app 

install:
	echo "install"

lint:
	echo "lint"

test:
	echo "test"

run_local:
	echo "run local"

docker_build:
	docker build --tag $(APP_NAME) .	

docker_run:
	docker run $(APP_NAME)

docker_sync:
	docker build --tag $(APP_NAME) .
	docker run $(APP_NAME)
