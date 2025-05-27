from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.orm import Session
from infrastructure.db.session import get_session
from infrastructure.db.repositories.marca_repository import MarcaRepositorySQLAlchemy
from core.entities.marca import Marca

router = APIRouter(
    prefix="/marca",
    tags=["Marca"],
)


def get_marca_repo(session: Session = Depends(get_session)) -> MarcaRepositorySQLAlchemy:
    return MarcaRepositorySQLAlchemy(session)


@router.get("/", response_model=List[Marca])
def listar_marcas(repo: MarcaRepositorySQLAlchemy = Depends(get_marca_repo)):
    return repo.list_all()


@router.get("/{idcodigo}", response_model=Marca)
def obter_marca(idcodigo: int, repo: MarcaRepositorySQLAlchemy = Depends(get_marca_repo)):
    marca = repo.get_by_id(idcodigo)
    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    return marca


@router.post("/", response_model=Marca, status_code=201)
def criar_marca(marc: Marca, repo: MarcaRepositorySQLAlchemy = Depends(get_marca_repo)):
    return repo.add(marc)


@router.put("/{idcodigo}", response_model=Marca)
def atualizar_marca(idcodigo: int, marc: Marca, repo: MarcaRepositorySQLAlchemy = Depends(get_marca_repo)):
    marc.IDCodigo = idcodigo
    return repo.update(marc)


@router.delete("/{idcodigo}", status_code=204)
def excluir_marca(idcodigo: int, repo: MarcaRepositorySQLAlchemy = Depends(get_marca_repo)):
    repo.delete(idcodigo)
    return None
