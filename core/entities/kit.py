from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Kit(BaseModel):
    IDCodigo: int | None = None
    Nome: str
    Descricao: str | None = None

    model_config = ConfigDict(from_attributes=True)


class KitMontado(BaseModel):
    IDCodigo: int | None = None
    IDKit: int
    IDProduto: int
    Quantidade: float

    model_config = ConfigDict(from_attributes=True)
