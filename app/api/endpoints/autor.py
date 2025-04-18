from fastapi import APIRouter, HTTPException, status
from typing import Dict
from schemas.autor_schema import Autor, AutorCreate

router = APIRouter()

autor_db: Dict[int, dict] = {}
next_id = 1

@router.post("/", response_model=Autor, status_code=status.HTTP_201_CREATED)
def create_autor(autor: AutorCreate):
    global next_id
    new_autor = autor.dict()
    new_autor['autor_id'] = next_id
    autor_db[next_id] = new_autor
    next_id += 1
    return new_autor

@router.get("/{autor_id}", response_model=Autor)
def read_autor(autor_id: int):
    if autor_id not in autor_db:
        raise HTTPException(status_code=404, detail="Author nicht gefunden")
    return autor_db[autor_id]

@router.put("/{autor_id}", response_model=Autor)
def update_autor(autor_id: int, autor: AutorCreate):
    if autor_id not in autor_db:
        raise HTTPException(status_code=404, detail="Author nicht gefunden")
    updated = autor.dict()
    updated['autor_id'] = autor_id
    autor_db[autor_id] = updated
    return updated

@router.delete("/{autor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_autor(autor_id: int):
    if autor_id not in autor_db:
        raise HTTPException(status_code=404, detail="Author nicht gefunden")
    del autor_db[autor_id]
    return
