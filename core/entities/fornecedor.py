# core/entities/fornecedor.py
from pydantic import BaseModel, ConfigDict

class Fornecedor(BaseModel):
    IDCodigo: int | None = None
    Nome: str
    CNPJ: str | None = None
    Telefone: str | None = None
    Email: str | None = None
    Endereco: str | None = None
    Observacao: str | None = None

    model_config = ConfigDict(from_attributes=True)
