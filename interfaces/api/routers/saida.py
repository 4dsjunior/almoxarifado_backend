from fastapi import APIRouter, Depends, HTTPException
from typing import List

from core.entities.saida import Saida
from infrastructure.db.session import get_session
from infrastructure.db.repositories import SaidaRepositorySQLAlchemy

router = APIRouter(prefix="/saida", tags=["Saída de Material"])


def get_saida_repo(session=Depends(get_session)):
    return SaidaRepositorySQLAlchemy(session)


@router.get("/", response_model=List[Saida])
def listar_saidas(repo=Depends(get_saida_repo)):
    return repo.list_all()


@router.get("/{idcodigo}", response_model=Saida)
def get_saida(idcodigo: int, repo=Depends(get_saida_repo)):
    saida = repo.get_by_id(idcodigo)
    if not saida:
        raise HTTPException(status_code=404, detail="Saída não encontrada")
    return saida


@router.post("/", response_model=Saida)
def add_saida(saida: Saida, repo=Depends(get_saida_repo)):
    return repo.add(saida)


@router.get("/produto/{id_produto}", response_model=List[Saida])
def listar_por_produto(id_produto: int, repo=Depends(get_saida_repo)):
    return repo.list_by_produto(id_produto)
