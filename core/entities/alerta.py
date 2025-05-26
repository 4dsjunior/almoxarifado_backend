from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Alerta(BaseModel):
    IDCodigo: int | None = None
    Tipo: str
    Mensagem: str
    DataCriacao: datetime

    model_config = ConfigDict(from_attributes=True)
