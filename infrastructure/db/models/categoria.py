# infrastructure/db/models/categorias.py
from sqlalchemy import Column, Integer, String
from .base import Base

class Tabela_TBCategorias(Base):
    __tablename__ = "Tabela_TBCategorias"
    IDCodigo = Column(Integer, primary_key=True)
    Nome = Column(String, unique=True, nullable=False)
