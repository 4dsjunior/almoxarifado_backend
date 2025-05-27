from pydantic import BaseModel, ConfigDict

class KitMontado(BaseModel):
    IDCodigo: int | None = None
    IDKit: int
    IDProduto: int
    Quantidade: float

    model_config = ConfigDict(from_attributes=True)
