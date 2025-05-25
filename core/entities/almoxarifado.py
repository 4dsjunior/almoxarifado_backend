# core/entities/almoxarifado.py
from pydantic import BaseModel, ConfigDict

class Almoxarifado(BaseModel):
    IDCodigo: int | None = None
    Nome: str
    Localizacao: str | None = None
    Responsavel: str | None = None

    model_config = ConfigDict(from_attributes=True)
