FROM python:3.10.4-slim

WORKDIR /api
COPY . /api

RUN apt update -y \
    && apt install -y build-essential gcc \
    && pip install -r requirements/prod.txt

EXPOSE 8000

CMD ["uvicorn", "asgi:app --reload"]