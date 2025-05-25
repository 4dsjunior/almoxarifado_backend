from fastapi import APIRouter, Depends, HTTPException
from typing import List

from core.entities.devolucao import Devolucao
from infrastructure.db.session import get_session
from infrastructure.db.repositories import DevolucaoRepositorySQLAlchemy

router = APIRouter(prefix="/devolucao", tags=["Devolução/Reentrada"])


def get_devolucao_repo(session=Depends(get_session)):
    return DevolucaoRepositorySQLAlchemy(session)


@router.get("/", response_model=List[Devolucao])
def listar_devolucoes(repo=Depends(get_devolucao_repo)):
    return repo.list_all()


@router.get("/{idcodigo}", response_model=Devolucao)
def get_devolucao(idcodigo: int, repo=Depends(get_devolucao_repo)):
    devolucao = repo.get_by_id(idcodigo)
    if not devolucao:
        raise HTTPException(status_code=404, detail="Devolução não encontrada")
    return devolucao


@router.post("/", response_model=Devolucao)
def add_devolucao(devolucao: Devolucao, repo=Depends(get_devolucao_repo)):
    return repo.add(devolucao)


@router.get("/produto/{id_produto}", response_model=List[Devolucao])
def listar_por_produto(id_produto: int, repo=Depends(get_devolucao_repo)):
    return repo.list_by_produto(id_produto)
