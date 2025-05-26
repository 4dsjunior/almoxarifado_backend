from sqlalchemy import Column, Integer, String
from .base import Base  # garanta que tem infrastructure/db/models/base.py


class Tabela_TBAlmoxarifados(Base):
    __tablename__ = "Tabela_TBAlmoxarifados"
    IDCodigo = Column(Integer, primary_key=True, index=True)
    Nome = Column(String, unique=True, nullable=False)
