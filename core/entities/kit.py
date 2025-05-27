from pydantic import BaseModel, ConfigDict

class Kit(BaseModel):
    IDCodigo: int | None = None
    Nome: str
    Descricao: str | None = None

    model_config = ConfigDict(from_attributes=True)
