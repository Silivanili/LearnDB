from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from typing import Dict
from schemas.kurs_schema import Kurs, KursCreate

router = APIRouter()

kurs_db: Dict[int, dict] = {}
next_id = 1

@router.post("/", response_model=Kurs, status_code=status.HTTP_201_CREATED)
def create_kurs(kurs: KursCreate):
    global next_id
    new_kurs = kurs.dict()
    new_kurs['kurs_id'] = next_id
    new_kurs['Zeit'] = datetime.utcnow()
    kurs_db[next_id] = new_kurs
    next_id += 1
    return new_kurs

@router.get("/{kurs_id}", response_model=Kurs)
def read_kurs(kurs_id: int):
    if kurs_id not in kurs_db:
        raise HTTPException(status_code=404, detail="Kurs nicht gefunden")
    return kurs_db[kurs_id]

@router.put("/{kurs_id}", response_model=Kurs)
def update_kurs(kurs_id: int, kurs: KursCreate):
    if kurs_id not in kurs_db:
        raise HTTPException(status_code=404, detail="Kurs nicht gefunden")
    updated = kurs.dict()
    updated['kurs_id'] = kurs_id
    updated['Zeit'] = kurs_db[kurs_id]['Zeit']
    kurs_db[kurs_id] = updated
    return updated

@router.delete("/{kurs_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_kurs(kurs_id: int):
    if kurs_id not in kurs_db:
        raise HTTPException(status_code=404, detail="Kurs nicht gefunden")
    del kurs_db[kurs_id]
    return
