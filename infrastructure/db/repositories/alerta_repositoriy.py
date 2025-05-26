from sqlalchemy.orm import Session
from infrastructure.db.models.alerta import Tabela_TBAlertas
from core.entities.alerta import Alerta
from typing import List, Optional


class AlertaRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Alerta]:
        db_obj = self.session.query(Tabela_TBAlertas).filter_by(
            IDCodigo=idcodigo).first()
        return Alerta.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Alerta]:
        objs = self.session.query(Tabela_TBAlertas).all()
        return [Alerta.model_validate(obj) for obj in objs]

    def add(self, alerta: Alerta) -> Alerta:
        db_obj = Tabela_TBAlertas(
            **alerta.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Alerta.model_validate(db_obj)

    def update(self, alerta: Alerta) -> Alerta:
        db_obj = self.session.query(Tabela_TBAlertas).filter_by(
            IDCodigo=alerta.IDCodigo).first()
        if not db_obj:
            raise ValueError("Alerta não encontrado")
        for field, value in alerta.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Alerta.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBAlertas).filter_by(
            IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()
