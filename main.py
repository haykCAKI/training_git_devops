from typing import Union

from fastapi import FastAPI

import random

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Hello World", 
        "Return": "Retornando o Docker como esperado"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.radiant(0, 100)}