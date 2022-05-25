import os

import uvicorn

from application.app import create_app

app = create_app('os.environ["FASTAPI_CONFIG"]')
# config = get_config()
# uvicorn.run(app, **config.)