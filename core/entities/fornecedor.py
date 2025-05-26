from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Fornecedor(BaseModel):
    IDCodigo: int | None = None
    Nome: str
    CNPJ: str | None = None
    Telefone: str | None = None
    Email: str | None = None
    Endereco: str | None = None

    model_config = ConfigDict(from_attributes=True)
