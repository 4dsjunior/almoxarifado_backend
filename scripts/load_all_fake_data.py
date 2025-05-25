from sqlalchemy.orm import Session
from infrastructure.db.session import engine

from infrastructure.db.models import Base
from infrastructure.db.session import engine

# Cria as tabelas automaticamente antes de inserir dados
Base.metadata.create_all(bind=engine)
print("Tabelas criadas/verificadas com sucesso!")

from infrastructure.db.models import (
    Tabela_TBEstoque, Tabela_TBEntradas, Tabela_TBSaidas, Tabela_TBDevolucoes,
    Tabela_TBClientes, Tabela_TBOrdemServico, Tabela_TBOrdemServicoProdutos,
    Tabela_TBKit, Tabela_TBKitMontado,
    Tabela_TBMarca, Tabela_TBModelo, Tabela_TBCategorias,
    Tabela_TBAlmoxarifados, Tabela_TBFornecedores, Tabela_TBFormaPagto
)
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import random

# Limpa e popula tudo!
def main():
    with Session(engine) as session:
        # Limpa tabelas (cuidado em produção!)
        for model in [
            Tabela_TBKitMontado, Tabela_TBKit, Tabela_TBOrdemServicoProdutos, Tabela_TBOrdemServico,
            Tabela_TBDevolucoes, Tabela_TBSaidas, Tabela_TBEntradas, Tabela_TBEstoque,
            Tabela_TBClientes, Tabela_TBMarca, Tabela_TBModelo, Tabela_TBCategorias,
            Tabela_TBAlmoxarifados, Tabela_TBFornecedores, Tabela_TBFormaPagto
        ]:
            session.query(model).delete()

        # Catálogos
        marcas = [Tabela_TBMarca(Nome="Bosch"), Tabela_TBMarca(Nome="Vonder")]
        modelos = [Tabela_TBModelo(Nome="ProFI"), Tabela_TBModelo(Nome="StdX")]
        categorias = [Tabela_TBCategorias(Nome="Ferramentas"), Tabela_TBCategorias(Nome="Elétrico")]
        almoxes = [Tabela_TBAlmoxarifados(Nome="Central"), Tabela_TBAlmoxarifados(Nome="Setor A")]
        fornecedores = [
            Tabela_TBFornecedores(Nome="Fornecedor A", CNPJ="12345678000101"),
            Tabela_TBFornecedores(Nome="Fornecedor B", CNPJ="98765432000199")
        ]
        formas = [Tabela_TBFormaPagto(Nome="Dinheiro"), Tabela_TBFormaPagto(Nome="Boleto")]
        session.add_all(marcas + modelos + categorias + almoxes + fornecedores + formas)
        session.commit()

        # Estoque
        estoque = [
            Tabela_TBEstoque(
                CodDeBarras=f"1000{i}", NomeProduto=f"Produto {i}", Descricao=f"Desc {i}",
                Categoria=categorias[i%2].Nome, Marca=marcas[i%2].Nome, Modelo=modelos[i%2].Nome,
                QtdeEstoque=random.randint(30, 80), Unidade="un", Prateleira="A1",
                Almoxarifado=almoxes[i%2].Nome, Foto=None
            ) for i in range(1, 5)
        ]
        session.add_all(estoque)
        session.commit()

        # Clientes
        clientes = [
            Tabela_TBClientes(Nome="João", Email="joao@email.com", Telefone="(11) 99999-1111", Documento="111.111.111-11", Endereco="Rua 1"),
            Tabela_TBClientes(Nome="Maria", Email="maria@email.com", Telefone="(11) 99999-2222", Documento="222.222.222-22", Endereco="Rua 2"),
        ]
        session.add_all(clientes)
        session.commit()

        # Entradas e Saídas
        entradas = []
        saidas = []
        for idx, prod in enumerate(estoque, 1):
            entradas.append(Tabela_TBEntradas(
                IDProduto=prod.IDCodigo, Quantidade=15+idx, DataEntrada=datetime.utcnow()-timedelta(days=10-idx),
                Fornecedor=fornecedores[0].Nome, NotaFiscal=f"NF-{100+idx}", Observacao="ok"
            ))
            saidas.append(Tabela_TBSaidas(
                IDProduto=prod.IDCodigo, Quantidade=2*idx, DataSaida=datetime.utcnow()-timedelta(days=idx),
                Destinatario=clientes[idx % 2].Nome, Observacao="uso"
            ))
        session.add_all(entradas + saidas)
        session.commit()

        # Devoluções
        devolucoes = [
            Tabela_TBDevolucoes(
                IDProduto=estoque[0].IDCodigo, Quantidade=1, DataDevolucao=datetime.utcnow()-timedelta(days=1),
                Origem=clientes[0].Nome, Observacao="Retorno parcial"
            )
        ]
        session.add_all(devolucoes)
        session.commit()

        # Ordens de Serviço
        os_list = [
            Tabela_TBOrdemServico(
                Numero=f"OS-00{i}", Descricao=f"Manutenção {i}", Solicitante=clientes[0].Nome,
                DataAbertura=datetime.utcnow()-timedelta(days=10*i), DataFechamento=None, Status="aberta"
            ) for i in range(1, 3)
        ]
        session.add_all(os_list)
        session.commit()

        # OS Produtos
        os_prods = [
            Tabela_TBOrdemServicoProdutos(
                IDOrdemServico=os_list[0].IDCodigo, IDProduto=estoque[0].IDCodigo, Quantidade=3, Observacao="Uso OS1"
            ),
            Tabela_TBOrdemServicoProdutos(
                IDOrdemServico=os_list[1].IDCodigo, IDProduto=estoque[1].IDCodigo, Quantidade=2, Observacao="Uso OS2"
            ),
        ]
        session.add_all(os_prods)
        session.commit()

        # Kits e Kits Montados
        kits = [
            Tabela_TBKit(Nome="Kit Elétrico", Descricao="Para elétrica"),
            Tabela_TBKit(Nome="Kit Mecânica", Descricao="Ferramentas mecânicas"),
        ]
        session.add_all(kits)
        session.commit()

        kits_montados = [
            Tabela_TBKitMontado(IDKit=kits[0].IDCodigo, IDProduto=estoque[0].IDCodigo, Quantidade=2),
            Tabela_TBKitMontado(IDKit=kits[1].IDCodigo, IDProduto=estoque[2].IDCodigo, Quantidade=1),
        ]
        session.add_all(kits_montados)
        session.commit()

        print("Banco populado com FAKE DATA para TODOS os módulos (catálogos, estoque, transações, clientes, OS, kits etc)!")

if __name__ == "__main__":
    main()
