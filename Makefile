install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black .

lint:
	pylint --disable=R,C ./api
	pylint --disable=R,C ./src

test:
	pytest tests.py

deploy:
	uvicorn api.main:app --reload

dockerize:
	DOCKER_BUILDKIT=1 docker build . -t model-api:v1 &&\
		docker run -p 8000:8000 model-api:v1

all: install format lint test deploy