# infrastructure/db/models.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Tabela_TBEstoque(Base):
    __tablename__ = "Tabela_TBEstoque"
    IDCodigo = Column(Integer, primary_key=True)
    CodDeBarras = Column(String, unique=True)
    NomeProduto = Column(String)
    Descricao = Column(String)
    Categoria = Column(String)
    Marca = Column(String)
    Modelo = Column(String)
    QtdeEstoque = Column(Float)
    Unidade = Column(String)
    Prateleira = Column(String)
    Almoxarifado = Column(String)
    Foto = Column(String)


class Tabela_TBEntradas(Base):
    __tablename__ = "Tabela_TBEntradas"
    IDCodigo = Column(Integer, primary_key=True)
    IDProduto = Column(Integer, ForeignKey("Tabela_TBEstoque.IDCodigo"))
    Quantidade = Column(Float)
    DataEntrada = Column(DateTime)
    Fornecedor = Column(String)
    NotaFiscal = Column(String)
    Observacao = Column(String)


class Tabela_TBSaidas(Base):
    __tablename__ = "Tabela_TBSaidas"
    IDCodigo = Column(Integer, primary_key=True)
    IDProduto = Column(Integer, ForeignKey("Tabela_TBEstoque.IDCodigo"))
    Quantidade = Column(Float)
    DataSaida = Column(DateTime)
    Destinatario = Column(String)
    Observacao = Column(String)


class Tabela_TBDevolucoes(Base):
    __tablename__ = "Tabela_TBDevolucoes"
    IDCodigo = Column(Integer, primary_key=True)
    IDProduto = Column(Integer, ForeignKey("Tabela_TBEstoque.IDCodigo"))
    Quantidade = Column(Float)
    DataDevolucao = Column(DateTime)
    Origem = Column(String)
    Observacao = Column(String)


class Tabela_TBClientes(Base):
    __tablename__ = "Tabela_TBClientes"
    IDCodigo = Column(Integer, primary_key=True)
    Nome = Column(String)
    Email = Column(String)
    Telefone = Column(String)
    Documento = Column(String)
    Endereco = Column(String)


class Tabela_TBOrdemServico(Base):
    __tablename__ = "Tabela_TBOrdemServico"
    IDCodigo = Column(Integer, primary_key=True)
    Numero = Column(String, unique=True)
    Descricao = Column(String)
    Solicitante = Column(String)
    DataAbertura = Column(DateTime)
    DataFechamento = Column(DateTime)
    Status = Column(String)


class Tabela_TBOrdemServicoProdutos(Base):
    __tablename__ = "Tabela_TBOrdemServicoProdutos"
    IDCodigo = Column(Integer, primary_key=True)
    IDOrdemServico = Column(Integer, ForeignKey(
        "Tabela_TBOrdemServico.IDCodigo"))
    IDProduto = Column(Integer, ForeignKey("Tabela_TBEstoque.IDCodigo"))
    Quantidade = Column(Float)
    Observacao = Column(String)


class Tabela_TBKit(Base):
    __tablename__ = "Tabela_TBKit"
    IDCodigo = Column(Integer, primary_key=True)
    Nome = Column(String)
    Descricao = Column(String)


class Tabela_TBKitMontado(Base):
    __tablename__ = "Tabela_TBKitMontado"
    IDCodigo = Column(Integer, primary_key=True)
    IDKit = Column(Integer, ForeignKey("Tabela_TBKit.IDCodigo"))
    IDProduto = Column(Integer, ForeignKey("Tabela_TBEstoque.IDCodigo"))
    Quantidade = Column(Float)


class Tabela_TBMarca(Base):
    __tablename__ = "Tabela_TBMarca"
    IDCodigo = Column(Integer, primary_key=True)
    Nome = Column(String, unique=True)


class Tabela_TBModelo(Base):
    __tablename__ = "Tabela_TBModelo"
    IDCodigo = Column(Integer, primary_key=True)
    Nome = Column(String, unique=True)


class Tabela_TBCategorias(Base):
    __tablename__ = "Tabela_TBCategorias"
    IDCodigo = Column(Integer, primary_key=True)
    Nome = Column(String, unique=True)


class Tabela_TBAlmoxarifados(Base):
    __tablename__ = "Tabela_TBAlmoxarifados"
    IDCodigo = Column(Integer, primary_key=True)
    Nome = Column(String, unique=True)


class Tabela_TBFornecedores(Base):
    __tablename__ = "Tabela_TBFornecedores"
    IDCodigo = Column(Integer, primary_key=True)
    Nome = Column(String)
    CNPJ = Column(String)
    Endereco = Column(String)
    Telefone = Column(String)
    Email = Column(String)


class Tabela_TBFormaPagto(Base):
    __tablename__ = "Tabela_TBFormaPagto"
    IDCodigo = Column(Integer, primary_key=True)
    Nome = Column(String, unique=True)


class Tabela_TBLogAlteracoes(Base):
    __tablename__ = "Tabela_TBLogAlteracoes"
    IDCodigo = Column(Integer, primary_key=True)
    NomeTabela = Column(String)
    Acao = Column(String)
    RegistroID = Column(Integer)
    Usuario = Column(String)
    DataHora = Column(DateTime)
    DetalheAnterior = Column(Text)
    DetalheNovo = Column(Text)
