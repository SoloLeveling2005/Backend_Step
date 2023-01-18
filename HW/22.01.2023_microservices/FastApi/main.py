import logging
from typing import Union

import uvicorn
from fastapi import FastAPI


HOST = '0.0.0.0'
PORT = int(6000)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/log/{info_log}")
def read_item(info_log: str):
    logging.basicConfig(level=logging.INFO, filename="logger.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.info(info_log)
    return {"status": 200}


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)