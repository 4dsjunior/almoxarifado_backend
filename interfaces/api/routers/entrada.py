from fastapi import APIRouter, Depends, HTTPException
from typing import List

from core.entities.entrada import Entrada
from infrastructure.db.session import get_session
from infrastructure.db.repositories import EntradaRepositorySQLAlchemy

router = APIRouter(prefix="/entrada", tags=["Entrada de Material"])

def get_entrada_repo(session=Depends(get_session)):
    return EntradaRepositorySQLAlchemy(session)

@router.get("/", response_model=List[Entrada])
def listar_entradas(repo=Depends(get_entrada_repo)):
    return repo.list_all()

@router.get("/{idcodigo}", response_model=Entrada)
def get_entrada(idcodigo: int, repo=Depends(get_entrada_repo)):
    entrada = repo.get_by_id(idcodigo)
    if not entrada:
        raise HTTPException(status_code=404, detail="Entrada não encontrada")
    return entrada

@router.post("/", response_model=Entrada)
def add_entrada(entrada: Entrada, repo=Depends(get_entrada_repo)):
    return repo.add(entrada)

@router.get("/produto/{id_produto}", response_model=List[Entrada])
def listar_por_produto(id_produto: int, repo=Depends(get_entrada_repo)):
    return repo.list_by_produto(id_produto)
