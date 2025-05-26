from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import List, Optional

from infrastructure.db.models.devolucao import Tabela_TBDevolucoes
from infrastructure.db.models.estoque import Tabela_TBEstoque
from core.entities.devolucao import Devolucao


class DevolucaoRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Devolucao]:
        db_obj = (
            self.session
            .query(Tabela_TBDevolucoes)
            .filter_by(IDCodigo=idcodigo)
            .first()
        )
        return Devolucao.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Devolucao]:
        objs = self.session.query(Tabela_TBDevolucoes).all()
        return [Devolucao.model_validate(obj) for obj in objs]

    def add(self, devolucao: Devolucao) -> Devolucao:
        # Atualiza o estoque antes de registrar a devolução
        estoque = (
            self.session
            .query(Tabela_TBEstoque)
            .filter_by(IDCodigo=devolucao.IDProduto)
            .first()
        )
        if not estoque:
            raise HTTPException(
                status_code=404, detail="Produto não encontrado no estoque")
        estoque.QtdeEstoque += devolucao.Quantidade

        # Registra a devolução
        db_obj = Tabela_TBDevolucoes(
            **devolucao.model_dump(exclude_unset=True, exclude={"IDCodigo"})
        )
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Devolucao.model_validate(db_obj)

    def list_by_produto(self, id_produto: int) -> List[Devolucao]:
        objs = (
            self.session
            .query(Tabela_TBDevolucoes)
            .filter_by(IDProduto=id_produto)
            .all()
        )
        return [Devolucao.model_validate(obj) for obj in objs]
