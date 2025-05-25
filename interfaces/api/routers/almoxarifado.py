from fastapi import APIRouter, Depends, HTTPException
from typing import List
from infrastructure.db.repositories import AlmoxarifadoRepositorySQLAlchemy
from core.entities.almoxarifado import Almoxarifado
from infrastructure.db.session import get_session

router = APIRouter(prefix="/almoxarifado", tags=["Almoxarifado"])

def get_repo(session=Depends(get_session)):
    return AlmoxarifadoRepositorySQLAlchemy(session)

@router.get("/", response_model=List[Almoxarifado])
def listar(repo=Depends(get_repo)):
    return repo.list_all()

@router.get("/{idcodigo}", response_model=Almoxarifado)
def get_by_id(idcodigo: int, repo=Depends(get_repo)):
    obj = repo.get_by_id(idcodigo)
    if not obj:
        raise HTTPException(status_code=404, detail="Almoxarifado não encontrado")
    return obj

@router.post("/", response_model=Almoxarifado)
def add(item: Almoxarifado, repo=Depends(get_repo)):
    return repo.add(item)

@router.put("/{idcodigo}", response_model=Almoxarifado)
def update(idcodigo: int, item: Almoxarifado, repo=Depends(get_repo)):
    item.IDCodigo = idcodigo
    return repo.update(item)

@router.delete("/{idcodigo}")
def delete(idcodigo: int, repo=Depends(get_repo)):
    repo.delete(idcodigo)
    return {"ok": True}
