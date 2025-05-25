from fastapi import FastAPI
from infrastructure.db.session import create_db_and_tables
from interfaces.api.routers import estoque, entrada, saida, devolucao, cliente, ordem_servico, ordem_servico_produto, kit, marca, modelo, categoria, almoxarifado, fornecedor, forma_pagto

app = FastAPI(
    title="Almoxarifado 11.0 Plus+ Backend",
    version="0.1.0"
)

# Inclui o router do estoque
app.include_router(estoque.router)
# Inclui o router da entrada
app.include_router(entrada.router)
# Inclui o router da saida
app.include_router(saida.router)
# Inclui o router da devolucao
app.include_router(devolucao.router)
# Inclui o router da devolucao
app.include_router(cliente.router)
# Inclui o router da OS
app.include_router(ordem_servico.router)
# Inclui o router da OS Produtos
app.include_router(ordem_servico_produto.router)
# Inclui o router do Kit
app.include_router(kit.router)

app.include_router(marca.router)
app.include_router(modelo.router)
app.include_router(categoria.router)
app.include_router(almoxarifado.router)
app.include_router(fornecedor.router)
app.include_router(forma_pagto.router)


@app.on_event("startup")
def on_startup():
    # Cria as tabelas no banco, se ainda não existirem
    create_db_and_tables()


@app.get("/")
def root():
    return {"msg": "Backend Almoxarifado 11.0 Plus+ pronto!"}
