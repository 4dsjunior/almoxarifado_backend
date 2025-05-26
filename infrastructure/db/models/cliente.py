from sqlalchemy import Column, Integer, String
# Certifique-se de ter o arquivo base.py com Base = declarative_base()
from .base import Base


class Tabela_TBClientes(Base):
    __tablename__ = "Tabela_TBClientes"
    IDCodigo = Column(Integer, primary_key=True, index=True)
    Nome = Column(String, nullable=False)
    Email = Column(String)
    Telefone = Column(String)
    Documento = Column(String)
    Endereco = Column(String)
