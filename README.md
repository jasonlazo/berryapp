FASTAPI_CONFIG=production uvicorn asgi:app --reload


python -m unittest tests/**/*.py