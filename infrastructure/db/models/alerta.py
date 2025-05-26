from sqlalchemy import Column, Integer, String, DateTime
from .base import Base  # Crie um base.py no mesmo diretório, com o declarative_base()


class Tabela_TBAlertas(Base):
    __tablename__ = "Tabela_TBAlertas"
    IDCodigo = Column(Integer, primary_key=True, index=True)
    Tipo = Column(String, nullable=False)
    Mensagem = Column(String, nullable=False)
    DataCriacao = Column(DateTime, nullable=False)
