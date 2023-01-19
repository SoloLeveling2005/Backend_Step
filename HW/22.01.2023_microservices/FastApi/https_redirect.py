import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse
import logging
from typing import Union
from subprocess import Popen
import uvicorn
from fastapi import FastAPI


app = FastAPI()


HOST = '192.168.0.29'
PORT = int(6002)

app = FastAPI()


@app.get("/home")
def read_root():
    return {"Hello": "World"}


@app.get("/log/{info_log}")
def read_item(info_log: str):
    logging.basicConfig(level=logging.INFO, filename="logger.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    logging.info(info_log)
    return {"status": 200}

if __name__ == '__main__':
    # Popen(['python', '-m', 'https_redirect'])
    uvicorn.run('https_redirect:app', port=PORT, host=HOST)