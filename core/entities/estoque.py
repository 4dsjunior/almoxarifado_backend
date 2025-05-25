from pydantic import BaseModel, ConfigDict
from typing import Optional


class Estoque(BaseModel):
    IDCodigo: Optional[int] = None
    CodDeBarras: str
    NomeProduto: str
    Descricao: Optional[str] = None
    Categoria: Optional[str] = None
    Marca: Optional[str] = None
    Modelo: Optional[str] = None
    QtdeEstoque: float = 0
    Unidade: Optional[str] = None
    Prateleira: Optional[str] = None
    Almoxarifado: Optional[str] = None
    Foto: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
