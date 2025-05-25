from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Saida(BaseModel):
    IDCodigo: int | None = None
    IDProduto: int
    Quantidade: float
    DataSaida: datetime | None = None
    Destinatario: str | None = None
    Observacao: str | None = None

    model_config = ConfigDict(from_attributes=True)
