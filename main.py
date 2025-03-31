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

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo Pydantic
class Item(BaseModel):
    nome: str
    descricao: Union[str, None] = None
    preco: float
    em_estoque: bool = True

# Dependência de autenticação
async def verificar_token(autorizacao: str = Header(...)):
    if autorizacao != "Bearer token-secreto":
        raise HTTPException(status_code=403, detail="Token inválido")

# Rotas
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    if item_id < 0:
        raise HTTPException(status_code=400, detail="ID do item não pode ser negativo")
    return {"item_id": item_id, "q": q}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 100)}

@app.post("/itens/")
async def criar_item(item: Item):
    item_id = random.randint(1, 1000)
    return {
        "mensagem": "Item criado com sucesso",
        "item_id": item_id,
        **item.dict()
    }

@app.get("/protegido/")
async def rota_protegida(token: str = Depends(verificar_token)):
    return {"mensagem": "Acesso permitido", "dados": "Informações sensíveis"}

@app.get("/delay/")
async def resposta_com_delay():
    await asyncio.sleep(2)
    return {"mensagem": "Resposta atrasada de propósito"}

@app.get("/health/")
async def health_check():
    return {
        "status": "up",
        "versao": app.version,
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/busca/")
async def buscar_itens(
    termo: str,
    limit: int = 10,
    offset: int = 0,
    ativos: bool = True
):
    resultados = [f"Item {i}" for i in range(offset, offset + limit)]
    return {
        "termo": termo,
        "total": 100,
        "resultados": resultados
    }