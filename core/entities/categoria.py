# core/entities/categoria.py
from pydantic import BaseModel, ConfigDict

class Categoria(BaseModel):
    IDCodigo: int | None = None
    Nome: str

    model_config = ConfigDict(from_attributes=True)
