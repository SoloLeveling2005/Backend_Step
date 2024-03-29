import logging
from typing import Union
from subprocess import Popen
import uvicorn
from fastapi import FastAPI


HOST = '192.168.0.29'
PORT = int(6000)

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
    Popen(['python', '-m', 'https_redirect'])
    uvicorn.run(
        'server:app', port=PORT, host=HOST,
        reload=True,
        ssl_keyfile='test/certificates/client.pem',
        ssl_certfile='test/certificates/client.pem')