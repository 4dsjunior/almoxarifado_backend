from pydantic import BaseModel, ConfigDict


class Cliente(BaseModel):
    IDCodigo: int | None = None
    Nome: str
    Email: str | None = None
    Telefone: str | None = None
    Documento: str | None = None
    Endereco: str | None = None

    model_config = ConfigDict(from_attributes=True)
