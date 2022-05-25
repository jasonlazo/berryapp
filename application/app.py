from dotenv import load_dotenv
from fastapi import FastAPI

from application.config import get_config



def load_env(config_name: str):
    config_path = f'config/{config_name}.env'
    load_dotenv(config_path)


def create_app(config_name: str):
    app = FastAPI()
    load_env(config_name)
    config_module = f"application.config.{config_name.capitalize()}Config"
    from application.rest.berry import router as berry_router
    app.include_router(berry_router)
    return app


SETTINGS = get_config()
