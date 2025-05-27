from sqlalchemy import Column, Integer, Float, ForeignKey
from .base import Base

class Tabela_TBKitMontado(Base):
    __tablename__ = "Tabela_TBKitMontado"

    IDCodigo  = Column(Integer, primary_key=True, index=True)
    IDKit      = Column(Integer, ForeignKey("Tabela_TBKit.IDCodigo"), nullable=False)
    IDProduto  = Column(Integer, ForeignKey("Tabela_TBEstoque.IDCodigo"), nullable=False)
    Quantidade = Column(Float, nullable=False)
