from pydantic import BaseModel, ConfigDict


class OrdemServicoProduto(BaseModel):
    IDCodigo: int | None = None
    IDOrdemServico: int
    IDProduto: int
    Quantidade: float
    Observacao: str | None = None

    model_config = ConfigDict(from_attributes=True)
