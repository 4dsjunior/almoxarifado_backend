from sqlalchemy import Column, Integer, String
from .base import Base

class Tabela_TBKit(Base):
    __tablename__ = "Tabela_TBKit"

    IDCodigo = Column(Integer, primary_key=True, index=True)
    Nome     = Column(String, nullable=False)
    Descricao= Column(String, nullable=True)
