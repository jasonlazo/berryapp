# Berry App

## Run tests

```
pip install -r requirements/test.txt

python -m unittest tests/**/*.py
```

## Run app locally

```
pip install -r requirements/dev.txt

uvicorn asgi:app --reload
```

## Build docker

```
docker build -t berryapp .

docker run -it -d --name=berryapp -p 8000:8000 berryapp

```

## Make request to service

```
curl http://localhost:8000/
curl http://localhost:8000/allBerryStats
```

