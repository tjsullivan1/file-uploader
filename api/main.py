from pathlib import Path

import fastapi

import json
import uvicorn
from fastapi.staticfiles import StaticFiles
from views import home
from api import file_api
from services import file_service

api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()


def configure_routing():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(file_api.router)


def configure_api_keys():
    file = Path("settings.json").absolute()
    if not file.exists():
        print(
            f"WARNING: {file} file not found. You cannot continue -- please see settings_Template.json"
        )
        raise Exception(
            "settings.json file not found. You cannot continue -- please see settings_Template.json"
        )

    with open("settings.json") as fin:
        settings = json.load(fin)
        file_service.conenction_string = settings.get("azure_storage_connection_string")


if __name__ == "__main__":
    configure()
    uvicorn.run(api, port=8000, host="127.0.0.1")
else:
    configure()
