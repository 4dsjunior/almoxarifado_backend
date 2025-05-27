from sqlalchemy.orm import Session
from typing import List, Optional

from infrastructure.db.models.entrada import Tabela_TBEntradas
from core.entities.entrada import Entrada

class EntradaRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Entrada]:
        db_obj = (
            self.session
            .query(Tabela_TBEntradas)
            .filter_by(IDCodigo=idcodigo)
            .first()
        )
        return Entrada.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Entrada]:
        objs = self.session.query(Tabela_TBEntradas).all()
        return [Entrada.model_validate(obj) for obj in objs]

    def add(self, entrada: Entrada) -> Entrada:
        db_obj = Tabela_TBEntradas(
            **entrada.model_dump(exclude_unset=True, exclude={"IDCodigo"})
        )
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Entrada.model_validate(db_obj)

    def list_by_produto(self, id_produto: int) -> List[Entrada]:
        objs = (
            self.session
            .query(Tabela_TBEntradas)
            .filter_by(IDProduto=id_produto)
            .all()
        )
        return [Entrada.model_validate(obj) for obj in objs]
