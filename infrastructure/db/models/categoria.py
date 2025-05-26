from sqlalchemy import Column, Integer, String
from .base import Base  # Certifique-se de que existe (ver instrução anterior!)


class Tabela_TBCategorias(Base):
    __tablename__ = "Tabela_TBCategorias"
    IDCodigo = Column(Integer, primary_key=True, index=True)
    Nome = Column(String, unique=True, nullable=False)
