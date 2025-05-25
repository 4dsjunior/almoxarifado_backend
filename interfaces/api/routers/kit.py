from fastapi import APIRouter, Depends, HTTPException
from typing import List
from infrastructure.db.session import get_session
from infrastructure.db.repositories import KitRepositorySQLAlchemy, KitMontadoRepositorySQLAlchemy
from core.entities.kit import Kit, KitMontado

router = APIRouter(prefix="/kit", tags=["Kit"])


def get_repo(session=Depends(get_session)):
    return KitRepositorySQLAlchemy(session)


@router.get("/", response_model=List[Kit])
def list_kits(repo=Depends(get_repo)):
    return repo.list_all()


@router.get("/{idcodigo}", response_model=Kit)
def get_kit(idcodigo: int, repo=Depends(get_repo)):
    item = repo.get_by_id(idcodigo)
    if not item:
        raise HTTPException(status_code=404, detail="Kit não encontrado")
    return item


@router.post("/", response_model=Kit)
def add_kit(kit: Kit, repo=Depends(get_repo)):
    return repo.add(kit)


@router.put("/{idcodigo}", response_model=Kit)
def update_kit(idcodigo: int, kit: Kit, repo=Depends(get_repo)):
    kit.IDCodigo = idcodigo
    return repo.update(kit)


@router.delete("/{idcodigo}")
def delete_kit(idcodigo: int, repo=Depends(get_repo)):
    repo.delete(idcodigo)
    return {"ok": True}

# --- KitMontado ---


@router.get("/montado/", response_model=List[KitMontado])
def list_montados(session=Depends(get_session)):
    repo = KitMontadoRepositorySQLAlchemy(session)
    return repo.list_all()


@router.get("/montado/by-kit/{idkit}", response_model=List[KitMontado])
def list_by_kit(idkit: int, session=Depends(get_session)):
    repo = KitMontadoRepositorySQLAlchemy(session)
    return repo.list_by_kit(idkit)


@router.post("/montado/", response_model=KitMontado)
def add_montado(item: KitMontado, session=Depends(get_session)):
    repo = KitMontadoRepositorySQLAlchemy(session)
    return repo.add(item)


@router.put("/montado/{idcodigo}", response_model=KitMontado)
def update_montado(idcodigo: int, item: KitMontado, session=Depends(get_session)):
    repo = KitMontadoRepositorySQLAlchemy(session)
    item.IDCodigo = idcodigo
    return repo.update(item)


@router.delete("/montado/{idcodigo}")
def delete_montado(idcodigo: int, session=Depends(get_session)):
    repo = KitMontadoRepositorySQLAlchemy(session)
    repo.delete(idcodigo)
    return {"ok": True}
