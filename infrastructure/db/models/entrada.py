from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey
from .base import Base

class Tabela_TBEntradas(Base):
    __tablename__ = "Tabela_TBEntradas"
    IDCodigo = Column(Integer, primary_key=True, index=True)
    IDProduto = Column(Integer, ForeignKey("Tabela_TBEstoque.IDCodigo"), nullable=False)
    Quantidade = Column(Float, nullable=False)
    DataEntrada = Column(DateTime, nullable=False)
    Fornecedor = Column(String, nullable=True)
    NotaFiscal = Column(String, nullable=True)
    Observacao = Column(String, nullable=True)
