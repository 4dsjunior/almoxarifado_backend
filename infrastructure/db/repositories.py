from infrastructure.db.models import (
    Tabela_TBClientes, Tabela_TBOrdemServicoProdutos, Tabela_TBOrdemServico,
    Tabela_TBKit, Tabela_TBKitMontado, Tabela_TBEstoque, Tabela_TBEntradas,
    Tabela_TBSaidas, Tabela_TBDevolucoes, Tabela_TBMarca, Tabela_TBModelo,
    Tabela_TBCategorias, Tabela_TBAlmoxarifados, Tabela_TBFornecedores, Tabela_TBFormaPagto
)
from core.entities.repositories import (
    ClienteRepository, OrdemServicoRepository, OrdemServicoProdutoRepository, KitRepository, KitMontadoRepository,
    EstoqueRepository, EntradaRepository, SaidaRepository, DevolucaoRepository
)
from core.entities.cliente import Cliente
from core.entities.saida import Saida
from core.entities.estoque import Estoque
from core.entities.entrada import Entrada
from core.entities.devolucao import Devolucao
from core.entities.ordem_servico import OrdemServico
from core.entities.ordem_servico_produto import OrdemServicoProduto
from core.entities.kit import Kit, KitMontado
from core.entities.marca import Marca
from core.entities.modelo import Modelo
from core.entities.categoria import Categoria
from core.entities.almoxarifado import Almoxarifado
from core.entities.fornecedor import Fornecedor
from core.entities.forma_pagto import FormaPagto

from fastapi import HTTPException
from typing import List, Optional
from sqlalchemy.orm import Session

# === ESTOQUE ===
class EstoqueRepositorySQLAlchemy(EstoqueRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Estoque]:
        db_obj = self.session.query(Tabela_TBEstoque).filter_by(IDCodigo=idcodigo).first()
        return Estoque.model_validate(db_obj) if db_obj else None

    def get_by_barcode(self, cod_de_barras: str) -> Optional[Estoque]:
        db_obj = self.session.query(Tabela_TBEstoque).filter_by(CodDeBarras=cod_de_barras).first()
        return Estoque.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Estoque]:
        objs = self.session.query(Tabela_TBEstoque).all()
        return [Estoque.model_validate(obj) for obj in objs]

    def add(self, item: Estoque) -> Estoque:
        db_obj = Tabela_TBEstoque(**item.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Estoque.model_validate(db_obj)

    def update(self, item: Estoque) -> Estoque:
        db_obj = self.session.query(Tabela_TBEstoque).filter_by(IDCodigo=item.IDCodigo).first()
        if not db_obj:
            raise ValueError("Estoque não encontrado")
        for field, value in item.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Estoque.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBEstoque).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

# === ENTRADA ===
class EntradaRepositorySQLAlchemy(EntradaRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Entrada]:
        db_obj = self.session.query(Tabela_TBEntradas).filter_by(IDCodigo=idcodigo).first()
        return Entrada.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Entrada]:
        objs = self.session.query(Tabela_TBEntradas).all()
        return [Entrada.model_validate(obj) for obj in objs]

    def add(self, entrada: Entrada) -> Entrada:
        db_obj = Tabela_TBEntradas(**entrada.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Entrada.model_validate(db_obj)

    def list_by_produto(self, id_produto: int) -> List[Entrada]:
        objs = self.session.query(Tabela_TBEntradas).filter_by(IDProduto=id_produto).all()
        return [Entrada.model_validate(obj) for obj in objs]

# === SAÍDA ===
class SaidaRepositorySQLAlchemy(SaidaRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Saida]:
        db_obj = self.session.query(Tabela_TBSaidas).filter_by(IDCodigo=idcodigo).first()
        return Saida.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Saida]:
        objs = self.session.query(Tabela_TBSaidas).all()
        return [Saida.model_validate(obj) for obj in objs]

    def add(self, saida: Saida) -> Saida:
        estoque = self.session.query(Tabela_TBEstoque).filter_by(IDCodigo=saida.IDProduto).first()
        if not estoque:
            raise HTTPException(status_code=404, detail="Produto não encontrado no estoque")
        if saida.Quantidade > estoque.QtdeEstoque:
            raise HTTPException(status_code=400, detail="Saldo insuficiente no estoque")
        estoque.QtdeEstoque -= saida.Quantidade
        db_obj = Tabela_TBSaidas(**saida.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Saida.model_validate(db_obj)

    def list_by_produto(self, id_produto: int) -> List[Saida]:
        objs = self.session.query(Tabela_TBSaidas).filter_by(IDProduto=id_produto).all()
        return [Saida.model_validate(obj) for obj in objs]

# === DEVOLUÇÃO ===
class DevolucaoRepositorySQLAlchemy(DevolucaoRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Devolucao]:
        db_obj = self.session.query(Tabela_TBDevolucoes).filter_by(IDCodigo=idcodigo).first()
        return Devolucao.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Devolucao]:
        objs = self.session.query(Tabela_TBDevolucoes).all()
        return [Devolucao.model_validate(obj) for obj in objs]

    def add(self, devolucao: Devolucao) -> Devolucao:
        estoque = self.session.query(Tabela_TBEstoque).filter_by(IDCodigo=devolucao.IDProduto).first()
        if not estoque:
            raise HTTPException(status_code=404, detail="Produto não encontrado no estoque")
        estoque.QtdeEstoque += devolucao.Quantidade
        db_obj = Tabela_TBDevolucoes(**devolucao.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Devolucao.model_validate(db_obj)

    def list_by_produto(self, id_produto: int) -> List[Devolucao]:
        objs = self.session.query(Tabela_TBDevolucoes).filter_by(IDProduto=id_produto).all()
        return [Devolucao.model_validate(obj) for obj in objs]

# === CLIENTE ===
class ClienteRepositorySQLAlchemy(ClienteRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Cliente]:
        db_obj = self.session.query(Tabela_TBClientes).filter_by(IDCodigo=idcodigo).first()
        return Cliente.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Cliente]:
        objs = self.session.query(Tabela_TBClientes).all()
        return [Cliente.model_validate(obj) for obj in objs]

    def add(self, cliente: Cliente) -> Cliente:
        db_obj = Tabela_TBClientes(**cliente.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Cliente.model_validate(db_obj)

    def update(self, cliente: Cliente) -> Cliente:
        db_obj = self.session.query(Tabela_TBClientes).filter_by(IDCodigo=cliente.IDCodigo).first()
        if not db_obj:
            raise ValueError("Cliente não encontrado")
        for field, value in cliente.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Cliente.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBClientes).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

# === ORDEM DE SERVIÇO ===
class OrdemServicoRepositorySQLAlchemy(OrdemServicoRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[OrdemServico]:
        db_obj = self.session.query(Tabela_TBOrdemServico).filter_by(IDCodigo=idcodigo).first()
        return OrdemServico.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[OrdemServico]:
        objs = self.session.query(Tabela_TBOrdemServico).all()
        return [OrdemServico.model_validate(obj) for obj in objs]

    def add(self, os: OrdemServico) -> OrdemServico:
        db_obj = Tabela_TBOrdemServico(**os.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return OrdemServico.model_validate(db_obj)

    def update(self, os: OrdemServico) -> OrdemServico:
        db_obj = self.session.query(Tabela_TBOrdemServico).filter_by(IDCodigo=os.IDCodigo).first()
        if not db_obj:
            raise ValueError("Ordem de Serviço não encontrada")
        for field, value in os.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return OrdemServico.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBOrdemServico).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

# === ORDEM DE SERVIÇO PRODUTOS ===
class OrdemServicoProdutoRepositorySQLAlchemy(OrdemServicoProdutoRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[OrdemServicoProduto]:
        db_obj = self.session.query(Tabela_TBOrdemServicoProdutos).filter_by(IDCodigo=idcodigo).first()
        return OrdemServicoProduto.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[OrdemServicoProduto]:
        objs = self.session.query(Tabela_TBOrdemServicoProdutos).all()
        return [OrdemServicoProduto.model_validate(obj) for obj in objs]

    def add(self, item: OrdemServicoProduto) -> OrdemServicoProduto:
        db_obj = Tabela_TBOrdemServicoProdutos(**item.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return OrdemServicoProduto.model_validate(db_obj)

    def update(self, item: OrdemServicoProduto) -> OrdemServicoProduto:
        db_obj = self.session.query(Tabela_TBOrdemServicoProdutos).filter_by(IDCodigo=item.IDCodigo).first()
        if not db_obj:
            raise ValueError("Registro não encontrado")
        for field, value in item.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return OrdemServicoProduto.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBOrdemServicoProdutos).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

    def list_by_ordem_servico(self, id_ordem: int) -> List[OrdemServicoProduto]:
        objs = self.session.query(Tabela_TBOrdemServicoProdutos).filter_by(IDOrdemServico=id_ordem).all()
        return [OrdemServicoProduto.model_validate(obj) for obj in objs]

# === KIT ===
class KitRepositorySQLAlchemy(KitRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Kit]:
        db_obj = self.session.query(Tabela_TBKit).filter_by(IDCodigo=idcodigo).first()
        return Kit.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Kit]:
        objs = self.session.query(Tabela_TBKit).all()
        return [Kit.model_validate(obj) for obj in objs]

    def add(self, kit: Kit) -> Kit:
        db_obj = Tabela_TBKit(**kit.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Kit.model_validate(db_obj)

    def update(self, kit: Kit) -> Kit:
        db_obj = self.session.query(Tabela_TBKit).filter_by(IDCodigo=kit.IDCodigo).first()
        if not db_obj:
            raise ValueError("Kit não encontrado")
        for field, value in kit.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Kit.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBKit).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

# === KIT MONTADO ===
class KitMontadoRepositorySQLAlchemy(KitMontadoRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[KitMontado]:
        db_obj = self.session.query(Tabela_TBKitMontado).filter_by(IDCodigo=idcodigo).first()
        return KitMontado.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[KitMontado]:
        objs = self.session.query(Tabela_TBKitMontado).all()
        return [KitMontado.model_validate(obj) for obj in objs]

    def add(self, item: KitMontado) -> KitMontado:
        db_obj = Tabela_TBKitMontado(**item.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return KitMontado.model_validate(db_obj)

    def update(self, item: KitMontado) -> KitMontado:
        db_obj = self.session.query(Tabela_TBKitMontado).filter_by(IDCodigo=item.IDCodigo).first()
        if not db_obj:
            raise ValueError("Kit Montado não encontrado")
        for field, value in item.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return KitMontado.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBKitMontado).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

    def list_by_kit(self, idkit: int) -> List[KitMontado]:
        objs = self.session.query(Tabela_TBKitMontado).filter_by(IDKit=idkit).all()
        return [KitMontado.model_validate(obj) for obj in objs]

# === MARCA ===
class MarcaRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Marca]:
        db_obj = self.session.query(Tabela_TBMarca).filter_by(IDCodigo=idcodigo).first()
        return Marca.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Marca]:
        objs = self.session.query(Tabela_TBMarca).all()
        return [Marca.model_validate(obj) for obj in objs]

    def add(self, marca: Marca) -> Marca:
        db_obj = Tabela_TBMarca(**marca.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Marca.model_validate(db_obj)

    def update(self, marca: Marca) -> Marca:
        db_obj = self.session.query(Tabela_TBMarca).filter_by(IDCodigo=marca.IDCodigo).first()
        if not db_obj:
            raise ValueError("Marca não encontrada")
        for field, value in marca.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Marca.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBMarca).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

# === MODELO ===
class ModeloRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Modelo]:
        db_obj = self.session.query(Tabela_TBModelo).filter_by(IDCodigo=idcodigo).first()
        return Modelo.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Modelo]:
        objs = self.session.query(Tabela_TBModelo).all()
        return [Modelo.model_validate(obj) for obj in objs]

    def add(self, modelo: Modelo) -> Modelo:
        db_obj = Tabela_TBModelo(**modelo.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Modelo.model_validate(db_obj)

    def update(self, modelo: Modelo) -> Modelo:
        db_obj = self.session.query(Tabela_TBModelo).filter_by(IDCodigo=modelo.IDCodigo).first()
        if not db_obj:
            raise ValueError("Modelo não encontrado")
        for field, value in modelo.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Modelo.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBModelo).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

# === CATEGORIA ===
class CategoriaRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Categoria]:
        db_obj = self.session.query(Tabela_TBCategorias).filter_by(IDCodigo=idcodigo).first()
        return Categoria.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Categoria]:
        objs = self.session.query(Tabela_TBCategorias).all()
        return [Categoria.model_validate(obj) for obj in objs]

    def add(self, categoria: Categoria) -> Categoria:
        db_obj = Tabela_TBCategorias(**categoria.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Categoria.model_validate(db_obj)

    def update(self, categoria: Categoria) -> Categoria:
        db_obj = self.session.query(Tabela_TBCategorias).filter_by(IDCodigo=categoria.IDCodigo).first()
        if not db_obj:
            raise ValueError("Categoria não encontrada")
        for field, value in categoria.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Categoria.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBCategorias).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

# === ALMOXARIFADO ===
class AlmoxarifadoRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Almoxarifado]:
        db_obj = self.session.query(Tabela_TBAlmoxarifados).filter_by(IDCodigo=idcodigo).first()
        return Almoxarifado.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Almoxarifado]:
        objs = self.session.query(Tabela_TBAlmoxarifados).all()
        return [Almoxarifado.model_validate(obj) for obj in objs]

    def add(self, almox: Almoxarifado) -> Almoxarifado:
        db_obj = Tabela_TBAlmoxarifados(**almox.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Almoxarifado.model_validate(db_obj)

    def update(self, almox: Almoxarifado) -> Almoxarifado:
        db_obj = self.session.query(Tabela_TBAlmoxarifados).filter_by(IDCodigo=almox.IDCodigo).first()
        if not db_obj:
            raise ValueError("Almoxarifado não encontrado")
        for field, value in almox.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Almoxarifado.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBAlmoxarifados).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

# === FORNECEDOR ===
class FornecedorRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Fornecedor]:
        db_obj = self.session.query(Tabela_TBFornecedores).filter_by(IDCodigo=idcodigo).first()
        return Fornecedor.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Fornecedor]:
        objs = self.session.query(Tabela_TBFornecedores).all()
        return [Fornecedor.model_validate(obj) for obj in objs]

    def add(self, forn: Fornecedor) -> Fornecedor:
        db_obj = Tabela_TBFornecedores(**forn.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Fornecedor.model_validate(db_obj)

    def update(self, forn: Fornecedor) -> Fornecedor:
        db_obj = self.session.query(Tabela_TBFornecedores).filter_by(IDCodigo=forn.IDCodigo).first()
        if not db_obj:
            raise ValueError("Fornecedor não encontrado")
        for field, value in forn.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Fornecedor.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBFornecedores).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

# === FORMA PAGAMENTO ===
class FormaPagtoRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[FormaPagto]:
        db_obj = self.session.query(Tabela_TBFormaPagto).filter_by(IDCodigo=idcodigo).first()
        return FormaPagto.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[FormaPagto]:
        objs = self.session.query(Tabela_TBFormaPagto).all()
        return [FormaPagto.model_validate(obj) for obj in objs]

    def add(self, forma: FormaPagto) -> FormaPagto:
        db_obj = Tabela_TBFormaPagto(**forma.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return FormaPagto.model_validate(db_obj)

    def update(self, forma: FormaPagto) -> FormaPagto:
        db_obj = self.session.query(Tabela_TBFormaPagto).filter_by(IDCodigo=forma.IDCodigo).first()
        if not db_obj:
            raise ValueError("Forma de Pagamento não encontrada")
        for field, value in forma.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return FormaPagto.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBFormaPagto).filter_by(IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()
