from pydantic import BaseModel, ConfigDict

class Marca(BaseModel):
    IDCodigo: int | None = None
    Nome: str

    model_config = ConfigDict(from_attributes=True)
