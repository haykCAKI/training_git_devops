from typing import Union

from fastapi import FastAPI
from fastapi import HTTPException

import random

app = FastAPI(
    title="API Teste",
    description="API Teste para pucpr DevOps",
    version="0.1.0"
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="ID do item não pode ser negativo")
    return {"item_id": item_id, "q": q}

@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 100)}