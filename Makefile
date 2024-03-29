install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black .

lint:
	pylint --disable=R,C ./api --ignore-paths=./api/tests.py
	pylint --disable=R,C ./src

test-api:
	pytest api/tests.py --disable-warnings  

deploy:
	uvicorn api.main:app --reload

dockerize:
	DOCKER_BUILDKIT=1 docker build . -t model-api:v1 &&\
		docker run -p 8000:8000 model-api:v1

all: install format lint test 