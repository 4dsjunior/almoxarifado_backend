from sqlalchemy.orm import Session
from typing import List, Optional

from infrastructure.db.models.kit import Tabela_TBKit
from core.entities.kit import Kit

class KitRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Kit]:
        db_obj = (
            self.session
            .query(Tabela_TBKit)
            .filter_by(IDCodigo=idcodigo)
            .first()
        )
        return Kit.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Kit]:
        objs = self.session.query(Tabela_TBKit).all()
        return [Kit.model_validate(obj) for obj in objs]

    def add(self, kit: Kit) -> Kit:
        db_obj = Tabela_TBKit(
            **kit.model_dump(exclude_unset=True, exclude={"IDCodigo"})
        )
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Kit.model_validate(db_obj)

    def update(self, kit: Kit) -> Kit:
        db_obj = (
            self.session
            .query(Tabela_TBKit)
            .filter_by(IDCodigo=kit.IDCodigo)
            .first()
        )
        if not db_obj:
            raise ValueError("Kit não encontrado")
        for field, value in kit.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Kit.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = (
            self.session
            .query(Tabela_TBKit)
            .filter_by(IDCodigo=idcodigo)
            .first()
        )
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()
