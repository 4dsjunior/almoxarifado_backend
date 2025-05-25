
# core/entities/marca.py
from pydantic import BaseModel, ConfigDict

class Marca(BaseModel):
    IDCodigo: int | None = None
    Nome: str
    Observacao: str | None = None

    model_config = ConfigDict(from_attributes=True)
