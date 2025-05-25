from fastapi import APIRouter, Depends, HTTPException
from typing import List
from infrastructure.db.repositories import FormaPagtoRepositorySQLAlchemy
from core.entities.forma_pagto import FormaPagto
from infrastructure.db.session import get_session

router = APIRouter(prefix="/forma_pagto", tags=["Forma Pagto"])

def get_repo(session=Depends(get_session)):
    return FormaPagtoRepositorySQLAlchemy(session)

@router.get("/", response_model=List[FormaPagto])
def listar(repo=Depends(get_repo)):
    return repo.list_all()

@router.get("/{idcodigo}", response_model=FormaPagto)
def get_by_id(idcodigo: int, repo=Depends(get_repo)):
    obj = repo.get_by_id(idcodigo)
    if not obj:
        raise HTTPException(status_code=404, detail="Forma de pagamento não encontrada")
    return obj

@router.post("/", response_model=FormaPagto)
def add(item: FormaPagto, repo=Depends(get_repo)):
    return repo.add(item)

@router.put("/{idcodigo}", response_model=FormaPagto)
def update(idcodigo: int, item: FormaPagto, repo=Depends(get_repo)):
    item.IDCodigo = idcodigo
    return repo.update(item)

@router.delete("/{idcodigo}")
def delete(idcodigo: int, repo=Depends(get_repo)):
    repo.delete(idcodigo)
    return {"ok": True}
