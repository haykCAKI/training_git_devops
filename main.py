from typing import Union
from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
import random
import asyncio
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API Teste",
    description="API Teste para pucpr DevOps",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    nome: str
    descricao: Union[str, None] = None
    preco: float
    em_estoque: bool = True

    
async def verificar_token(autorizacao: str = Header(...)):
    if autorizacao != "Bearer token-secreto":
        raise HTTPException(status_code=403, detail="Token inválido")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.radiant(0, 100)}


@app.get("/busca/")
async def buscar_itens(
    termo: str,
    limit: int = 10,
    offset: int = 0,
    ativos: bool = True
):
    # Simulação de busca
    resultados = [f"Item {i}" for i in range(offset, offset + limit)]
    return {
        "termo": termo,
        "total": 100,  # Simulado
        "resultados": resultados
    }