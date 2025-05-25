from sqlalchemy.orm import sessionmaker
from infrastructure.db.session import engine
from infrastructure.db.models import (
    Tabela_TBEstoque,
    Tabela_TBEntradas,
    Tabela_TBSaidas,
    Tabela_TBDevolucoes,
)
from datetime import datetime

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

# --- ESTOQUE (PRODUTOS) ---
estoque_items = [
    Tabela_TBEstoque(
        IDCodigo=1,
        CodDeBarras="10001",
        NomeProduto="Chave de Fenda",
        Descricao="Chave de fenda simples",
        Categoria="Ferramenta",
        Marca="Tramontina",
        Modelo="123",
        QtdeEstoque=50,
        Unidade="UN",
        Prateleira="A1",
        Almoxarifado="Mecânica",
        Foto="",
    ),
    Tabela_TBEstoque(
        IDCodigo=2,
        CodDeBarras="10002",
        NomeProduto="Martelo",
        Descricao="Martelo de aço",
        Categoria="Ferramenta",
        Marca="Vonder",
        Modelo="M12",
        QtdeEstoque=25,
        Unidade="UN",
        Prateleira="A2",
        Almoxarifado="Mecânica",
        Foto="",
    ),
    Tabela_TBEstoque(
        IDCodigo=3,
        CodDeBarras="10003",
        NomeProduto="Rolamento Industrial",
        Descricao="Rolamento 6203",
        Categoria="Rolamento",
        Marca="SKF",
        Modelo="6203",
        QtdeEstoque=100,
        Unidade="UN",
        Prateleira="B1",
        Almoxarifado="Mecânica",
        Foto="",
    ),
    Tabela_TBEstoque(
        IDCodigo=4,
        CodDeBarras="10004",
        NomeProduto="Lubrificante Sintético",
        Descricao="Óleo sintético alta performance",
        Categoria="Lubrificante",
        Marca="Shell",
        Modelo="LubeX",
        QtdeEstoque=200,
        Unidade="L",
        Prateleira="B2",
        Almoxarifado="Mecânica",
        Foto="",
    ),
]

for item in estoque_items:
    db.merge(item)
db.commit()
print("Estoque populado.")

# --- ENTRADAS ---
entradas = [
    Tabela_TBEntradas(
        IDCodigo=1,
        IDProduto=1,
        Quantidade=10,
        DataEntrada=datetime(2024, 6, 5),
        Fornecedor="Ferramentas SA",
        NotaFiscal="NF12345",
        Observacao="Reposição básica",
    ),
    Tabela_TBEntradas(
        IDCodigo=2,
        IDProduto=3,
        Quantidade=20,
        DataEntrada=datetime(2024, 6, 4),
        Fornecedor="Mecânica Ltda",
        NotaFiscal="NF98765",
        Observacao="Recebido Mecânica",
    ),
]

for item in entradas:
    db.merge(item)
db.commit()
print("Entradas populadas.")

# --- SAÍDAS ---
saidas = [
    Tabela_TBSaidas(
        IDCodigo=1,
        IDProduto=1,
        Quantidade=5,
        DataSaida=datetime(2024, 6, 6),
        Destinatario="Manutenção",
        Observacao="Troca preventiva",
    ),
    Tabela_TBSaidas(
        IDCodigo=2,
        IDProduto=3,
        Quantidade=10,
        DataSaida=datetime(2024, 6, 5),
        Destinatario="Linha Produção",
        Observacao="Reparo emergencial",
    ),
]

for item in saidas:
    db.merge(item)
db.commit()
print("Saídas populadas.")

# --- DEVOLUÇÕES ---
devolucoes = [
    Tabela_TBDevolucoes(
        IDCodigo=1,
        IDProduto=1,
        Quantidade=1,
        DataDevolucao=datetime(2024, 6, 7),
        Origem="Manutenção",
        Observacao="Material não utilizado",
    ),
    Tabela_TBDevolucoes(
        IDCodigo=2,
        IDProduto=4,
        Quantidade=5,
        DataDevolucao=datetime(2024, 6, 8),
        Origem="Lubrificação",
        Observacao="Sobra de aplicação",
    ),
]

for item in devolucoes:
    db.merge(item)
db.commit()
print("Devoluções populadas.")

print("Banco populado com dados fictícios! Pronto para testar API.")
