APP_NAME := python-app 

install:
	echo "install"

lint:
	echo "lint"

test:
	echo "test"

run:
	python3 -m src

docker_run:
	docker run $(APP_NAME)

docker_refresh:
	docker build --tag $(APP_NAME) .
	docker run $(APP_NAME)
