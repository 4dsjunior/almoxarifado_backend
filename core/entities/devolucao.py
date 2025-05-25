from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Devolucao(BaseModel):
    IDCodigo: int | None = None
    IDProduto: int
    Quantidade: float
    DataDevolucao: datetime | None = None
    Origem: str | None = None
    Observacao: str | None = None

    model_config = ConfigDict(from_attributes=True)
