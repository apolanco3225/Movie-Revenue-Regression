# Movie-Revenue-Regression


Execute the API:
```
uvicorn api.main:app --reload
```

Build and run docker image
```
DOCKER_BUILDKIT=1 docker build . -t model-api:v1 
docker run -p 8000:8000 model-api:v1
```