from fastapi import FastAPI
from infrastructure.db.session import create_db_and_tables

# Routers
from interfaces.api.routers.almoxarifado import router as almoxarifado_router
from interfaces.api.routers.categoria import router as categoria_router
from interfaces.api.routers.cliente import router as cliente_router
from interfaces.api.routers.entrada import router as entrada_router
from interfaces.api.routers.estoque import router as estoque_router
from interfaces.api.routers.fornecedor import router as fornecedor_router
from interfaces.api.routers.forma_pagto import router as forma_pagto_router
from interfaces.api.routers.kit import router as kit_router
from interfaces.api.routers.marca import router as marca_router
from interfaces.api.routers.modelo import router as modelo_router
from interfaces.api.routers.ordem_servico import router as os_router
from interfaces.api.routers.ordem_servico_produto import router as osp_router
from interfaces.api.routers.saida import router as saida_router
from interfaces.api.routers.devolucao import router as devolucao_router

app = FastAPI(
    title="Almoxarifado 11.0 Plus+ Backend",
    version="0.1.0",
)

# Inclui todos os routers em ordem alfabética de prefix
app.include_router(almoxarifado_router)
app.include_router(categoria_router)
app.include_router(cliente_router)
app.include_router(entrada_router)
app.include_router(estoque_router)
app.include_router(fornecedor_router)
app.include_router(forma_pagto_router)
app.include_router(kit_router)
app.include_router(marca_router)
app.include_router(modelo_router)
app.include_router(os_router)
app.include_router(osp_router)
app.include_router(saida_router)
app.include_router(devolucao_router)


@app.on_event("startup")
def on_startup():
    # Cria as tabelas no banco, se ainda não existirem
    create_db_and_tables()


@app.get("/", tags=["Root"])
def root():
    return {"msg": "Backend Almoxarifado 11.0 Plus+ pronto!"}
