from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from typing import Dict
from schemas.karteikarte_schema import Karteikarte, KarteikarteCreate

router = APIRouter()

karteikarte_db: Dict[int, dict] = {}
next_id = 1

@router.post("/", response_model=Karteikarte, status_code=status.HTTP_201_CREATED)
def create_karteikarte(karteikarte: KarteikarteCreate):
    global next_id
    new_karteikarte = karteikarte.dict()
    new_karteikarte['kartei_id'] = next_id
    new_karteikarte['erstellungsdatum'] = datetime.utcnow()
    karteikarte_db[next_id] = new_karteikarte
    next_id += 1
    return new_karteikarte

@router.get("/{kartei_id}", response_model=Karteikarte)
def read_karteikarte(kartei_id: int):
    if kartei_id not in karteikarte_db:
        raise HTTPException(status_code=404, detail="Karteikarte nicht gefunden")
    return karteikarte_db[kartei_id]

@router.put("/{kartei_id}", response_model=Karteikarte)
def update_karteikarte(kartei_id: int, karteikarte: KarteikarteCreate):
    if kartei_id not in karteikarte_db:
        raise HTTPException(status_code=404, detail="Karteikarte nicht gefunden")
    updated = karteikarte.dict()
    updated['kartei_id'] = kartei_id
    updated['erstellungsdatum'] = karteikarte_db[kartei_id]['erstellungsdatum']
    karteikarte_db[kartei_id] = updated
    return updated

@router.delete("/{kartei_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_karteikarte(kartei_id: int):
    if kartei_id not in karteikarte_db:
        raise HTTPException(status_code=404, detail="Karteikarte nicht gefunden")
    del karteikarte_db[kartei_id]
    return
