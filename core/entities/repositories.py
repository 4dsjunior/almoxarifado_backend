from core.entities.saida import Saida
from core.entities.estoque import Estoque
from core.entities.entrada import Entrada
from core.entities.cliente import Cliente
from core.entities.devolucao import Devolucao
from core.entities.kit import Kit, KitMontado
from core.entities.ordem_servico import OrdemServico
from core.entities.ordem_servico_produto import OrdemServicoProduto
from typing import Protocol, List, Optional


class EstoqueRepository(Protocol):
    def get_by_id(self, idcodigo: int) -> Optional[Estoque]:
        ...

    def list_all(self) -> List[Estoque]:
        ...

    def add(self, item: Estoque) -> Estoque:
        ...

    def update(self, item: Estoque) -> Estoque:
        ...

    def delete(self, idcodigo: int) -> None:
        ...


class EntradaRepository(Protocol):
    """Contrato para movimentação de entradas de produtos."""

    def get_by_id(self, idcodigo: int) -> Optional[Entrada]:
        ...

    def list_all(self) -> List[Entrada]:
        ...

    def add(self, entrada: Entrada) -> Entrada:
        ...

    def list_by_produto(self, id_produto: int) -> List[Entrada]:
        ...


class SaidaRepository(Protocol):
    def get_by_id(self, idcodigo: int) -> Optional[Saida]:
        ...

    def list_all(self) -> List[Saida]:
        ...

    def add(self, saida: Saida) -> Saida:
        ...

    def list_by_produto(self, id_produto: int) -> List[Saida]:
        ...


class DevolucaoRepository(Protocol):
    def get_by_id(self, idcodigo: int) -> Optional[Devolucao]:
        ...

    def list_all(self) -> List[Devolucao]:
        ...

    def add(self, devolucao: Devolucao) -> Devolucao:
        ...

    def list_by_produto(self, id_produto: int) -> List[Devolucao]:
        ...


class ClienteRepository(Protocol):
    def get_by_id(self, idcodigo: int) -> Optional[Cliente]:
        ...

    def list_all(self) -> List[Cliente]:
        ...

    def add(self, cliente: Cliente) -> Cliente:
        ...

    def update(self, cliente: Cliente) -> Cliente:
        ...

    def delete(self, idcodigo: int) -> None:
        ...


class OrdemServicoRepository(Protocol):
    def get_by_id(self, idcodigo: int) -> Optional[OrdemServico]:
        ...

    def list_all(self) -> List[OrdemServico]:
        ...

    def add(self, os: OrdemServico) -> OrdemServico:
        ...

    def update(self, os: OrdemServico) -> OrdemServico:
        ...

    def delete(self, idcodigo: int) -> None:
        ...


class OrdemServicoProdutoRepository(Protocol):
    def get_by_id(self, idcodigo: int) -> Optional[OrdemServicoProduto]:
        ...

    def list_all(self) -> List[OrdemServicoProduto]:
        ...

    def add(self, item: OrdemServicoProduto) -> OrdemServicoProduto:
        ...

    def update(self, item: OrdemServicoProduto) -> OrdemServicoProduto:
        ...

    def delete(self, idcodigo: int) -> None:
        ...

    def list_by_ordem_servico(
            self, id_ordem: int) -> List[OrdemServicoProduto]:
        ...


class KitRepository(Protocol):
    def get_by_id(self, idcodigo: int) -> Optional[Kit]:
        ...

    def list_all(self) -> List[Kit]:
        ...

    def add(self, kit: Kit) -> Kit:
        ...

    def update(self, kit: Kit) -> Kit:
        ...

    def delete(self, idcodigo: int) -> None:
        ...


class KitMontadoRepository(Protocol):
    def get_by_id(self, idcodigo: int) -> Optional[KitMontado]:
        ...

    def list_all(self) -> List[KitMontado]:
        ...

    def add(self, item: KitMontado) -> KitMontado:
        ...

    def update(self, item: KitMontado) -> KitMontado:
        ...

    def delete(self, idcodigo: int) -> None:
        ...

    def list_by_kit(self, idkit: int) -> List[KitMontado]:
        ...
