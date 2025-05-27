from sqlalchemy.orm import Session
from typing import List, Optional

from infrastructure.db.models.kit_montado import Tabela_TBKitMontado
from core.entities.kit import KitMontado

class KitMontadoRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[KitMontado]:
        db_obj = (
            self.session
            .query(Tabela_TBKitMontado)
            .filter_by(IDCodigo=idcodigo)
            .first()
        )
        return KitMontado.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[KitMontado]:
        objs = self.session.query(Tabela_TBKitMontado).all()
        return [KitMontado.model_validate(obj) for obj in objs]

    def add(self, item: KitMontado) -> KitMontado:
        db_obj = Tabela_TBKitMontado(
            **item.model_dump(exclude_unset=True, exclude={"IDCodigo"})
        )
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return KitMontado.model_validate(db_obj)

    def update(self, item: KitMontado) -> KitMontado:
        db_obj = (
            self.session
            .query(Tabela_TBKitMontado)
            .filter_by(IDCodigo=item.IDCodigo)
            .first()
        )
        if not db_obj:
            raise ValueError("Kit Montado não encontrado")
        for field, value in item.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return KitMontado.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = (
            self.session
            .query(Tabela_TBKitMontado)
            .filter_by(IDCodigo=idcodigo)
            .first()
        )
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()

    def list_by_kit(self, idkit: int) -> List[KitMontado]:
        objs = (
            self.session
            .query(Tabela_TBKitMontado)
            .filter_by(IDKit=idkit)
            .all()
        )
        return [KitMontado.model_validate(obj) for obj in objs]
