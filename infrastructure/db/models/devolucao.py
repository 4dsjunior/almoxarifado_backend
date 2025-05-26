from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey
from .base import Base  # Base gerado em infrastructure/db/models/base.py


class Tabela_TBDevolucoes(Base):
    __tablename__ = "Tabela_TBDevolucoes"
    IDCodigo = Column(Integer, primary_key=True, index=True)
    IDProduto = Column(Integer, ForeignKey(
        "Tabela_TBEstoque.IDCodigo"), nullable=False)
    Quantidade = Column(Float, nullable=False)
    DataDevolucao = Column(DateTime, nullable=False)
    Origem = Column(String, nullable=True)
    Observacao = Column(String, nullable=True)
