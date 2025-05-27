from sqlalchemy import Column, Integer, String
from .base import Base

class Tabela_TBMarca(Base):
    __tablename__ = "Tabela_TBMarca"

    IDCodigo = Column(Integer, primary_key=True, index=True)
    Nome = Column(String, unique=True, nullable=False)
