from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime


Base = declarative_base()


class Tabela_TBEstoque(Base):
    __tablename__ = "Tabela_TBEstoque"
    IDCodigo = Column(Integer, primary_key=True, autoincrement=True)
    CodDeBarras = Column(String, unique=True, nullable=False)
    NomeProduto = Column(String, nullable=False)
    Descricao = Column(String)
    Categoria = Column(String)
    Marca = Column(String)
    Modelo = Column(String)
    QtdeEstoque = Column(Float, default=0)
    Unidade = Column(String)
    Prateleira = Column(String)
    Almoxarifado = Column(String)
    Foto = Column(String)


class Tabela_TBEntradas(Base):
    __tablename__ = "Tabela_TBEntradas"
    IDCodigo = Column(Integer, primary_key=True, autoincrement=True)
    IDProduto = Column(Integer, ForeignKey(
        "Tabela_TBEstoque.IDCodigo"), nullable=False)
    Quantidade = Column(Float, nullable=False)
    DataEntrada = Column(DateTime, default=datetime.utcnow)
    Fornecedor = Column(String)
    NotaFiscal = Column(String)
    Observacao = Column(String)


class Tabela_TBSaidas(Base):
    __tablename__ = "Tabela_TBSaidas"
    IDCodigo = Column(Integer, primary_key=True, autoincrement=True)
    IDProduto = Column(Integer, ForeignKey(
        "Tabela_TBEstoque.IDCodigo"), nullable=False)
    Quantidade = Column(Float, nullable=False)
    DataSaida = Column(DateTime, default=datetime.utcnow)
    Destinatario = Column(String)
    Observacao = Column(String)


class Tabela_TBDevolucoes(Base):
    __tablename__ = "Tabela_TBDevolucoes"
    IDCodigo = Column(Integer, primary_key=True, autoincrement=True)
    IDProduto = Column(Integer, ForeignKey(
        "Tabela_TBEstoque.IDCodigo"), nullable=False)
    Quantidade = Column(Float, nullable=False)
    DataDevolucao = Column(DateTime, default=datetime.utcnow)
    Origem = Column(String)
    Observacao = Column(String)


class Tabela_TBClientes(Base):
    __tablename__ = "Tabela_TBClientes"
    IDCodigo = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String, nullable=False)
    Email = Column(String)
    Telefone = Column(String)
    Documento = Column(String)
    Endereco = Column(String)


class Tabela_TBOrdemServico(Base):
    __tablename__ = "Tabela_TBOrdemServico"
    IDCodigo = Column(Integer, primary_key=True, autoincrement=True)
    Numero = Column(String, unique=True, nullable=False)
    Descricao = Column(String)
    Solicitante = Column(String)
    DataAbertura = Column(DateTime)
    DataFechamento = Column(DateTime)
    Status = Column(String)


class Tabela_TBOrdemServicoProdutos(Base):
    __tablename__ = "Tabela_TBOrdemServicoProdutos"
    IDCodigo = Column(Integer, primary_key=True, autoincrement=True)
    IDOrdemServico = Column(Integer, ForeignKey(
        "Tabela_TBOrdemServico.IDCodigo"), nullable=False)
    IDProduto = Column(Integer, ForeignKey(
        "Tabela_TBEstoque.IDCodigo"), nullable=False)
    Quantidade = Column(Float, nullable=False)
    Observacao = Column(String)


class Tabela_TBKit(Base):
    __tablename__ = "Tabela_TBKit"
    IDCodigo = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String, nullable=False)
    Descricao = Column(String)


class Tabela_TBKitMontado(Base):
    __tablename__ = "Tabela_TBKitMontado"
    IDCodigo = Column(Integer, primary_key=True, autoincrement=True)
    IDKit = Column(Integer, ForeignKey(
        "Tabela_TBKit.IDCodigo"), nullable=False)
    IDProduto = Column(Integer, ForeignKey(
        "Tabela_TBEstoque.IDCodigo"), nullable=False)
    Quantidade = Column(Float, nullable=False)
