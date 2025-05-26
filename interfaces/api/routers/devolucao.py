# interfaces/api/routers/devolucao.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.orm import Session
from infrastructure.db.session import get_session
from core.entities.devolucao import Devolucao
from infrastructure.db.repositories.devolucao_repository import DevolucaoRepositorySQLAlchemy

router = APIRouter(prefix="/devolucoes", tags=["Devoluções"])


def get_devolucao_repo(session: Session = Depends(get_session)):
    return DevolucaoRepositorySQLAlchemy(session)


@router.get("/", response_model=List[Devolucao])
def listar_devolucoes(repo=Depends(get_devolucao_repo)):
    return repo.list_all()


@router.get("/{idcodigo}", response_model=Devolucao)
def get_devolucao(idcodigo: int, repo=Depends(get_devolucao_repo)):
    obj = repo.get_by_id(idcodigo)
    if not obj:
        raise HTTPException(status_code=404, detail="Devolução não encontrada")
    return obj


@router.post("/", response_model=Devolucao)
def add_devolucao(devolucao: Devolucao, repo=Depends(get_devolucao_repo)):
    return repo.add(devolucao)


@router.get("/produto/{id_produto}", response_model=List[Devolucao])
def listar_por_produto(id_produto: int, repo=Depends(get_devolucao_repo)):
    return repo.list_by_produto(id_produto)
