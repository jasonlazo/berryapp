FROM python:3.10.4-slim

ENV PORT=8000

WORKDIR /api
COPY . /api

RUN apt update -y \
    && apt install -y build-essential gcc \
    && pip install -r requirements/prod.txt

EXPOSE $PORT

CMD uvicorn asgi:app --host=0.0.0.0 --port=$PORT