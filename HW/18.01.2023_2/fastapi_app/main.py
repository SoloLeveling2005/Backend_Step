from typing import Union
import logging
from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('logger.log')
handler.setLevel(logging.INFO)
logger.addHandler(handler)

@app.get("/new_log/{info}")
def read_item(info: str, q: Union[str, None] = None):
    logger.info(info)