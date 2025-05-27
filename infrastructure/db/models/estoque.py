from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Tabela_TBEstoque(Base):
    __tablename__ = "Tabela_TBEstoque"
    IDCodigo = Column(Integer, primary_key=True, index=True)
    CodDeBarras = Column(String, unique=True, nullable=False)
    NomeProduto  = Column(String, nullable=False)
    Descricao    = Column(String, nullable=True)
    Categoria    = Column(String, nullable=True)
    Marca        = Column(String, nullable=True)
    Modelo       = Column(String, nullable=True)
    QtdeEstoque  = Column(Float, default=0.0, nullable=False)
    Unidade      = Column(String, nullable=True)
    Prateleira   = Column(String, nullable=True)
    Almoxarifado = Column(String, nullable=True)
    Foto         = Column(String, nullable=True)
