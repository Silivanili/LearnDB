from fastapi import APIRouter, HTTPException, status
from typing import Dict
from schemas.benutzer_schema import Benutzer, BenutzerCreate

router = APIRouter()

benutzer_db: Dict[int, dict] = {}
next_id = 1

@router.post("/", response_model=Benutzer, status_code=status.HTTP_201_CREATED)
def create_benutzer(benutzer: BenutzerCreate):
    global next_id
    new_benutzer = benutzer.dict()
    new_benutzer['benutzer_id'] = next_id
    benutzer_db[next_id] = new_benutzer
    next_id += 1
    return new_benutzer

@router.get("/{benutzer_id}", response_model=Benutzer)
def read_benutzer(benutzer_id: int):
    if benutzer_id not in benutzer_db:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    return benutzer_db[benutzer_id]

@router.put("/{benutzer_id}", response_model=Benutzer)
def update_benutzer(benutzer_id: int, benutzer: BenutzerCreate):
    if benutzer_id not in benutzer_db:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    updated = benutzer.dict()
    updated['benutzer_id'] = benutzer_id
    benutzer_db[benutzer_id] = updated
    return updated

@router.delete("/{benutzer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_benutzer(benutzer_id: int):
    if benutzer_id not in benutzer_db:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    del benutzer_db[benutzer_id]
    return
