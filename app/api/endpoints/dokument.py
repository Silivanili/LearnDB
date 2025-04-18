from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from typing import List
from schemas.dokument_schema import Dokument, DokumentCreate

router = APIRouter()

dokument_db = {}
next_id = 1

@router.post("/", response_model=Dokument, status_code=status.HTTP_201_CREATED)
def create_dokument(dokument: DokumentCreate):
    global next_id
    new_dokument = dokument.dict()
    new_dokument['document_id'] = next_id
    new_dokument['erstellungsdatum'] = datetime.utcnow()
    dokument_db[next_id] = new_dokument
    next_id += 1
    return new_dokument

@router.get("/{document_id}", response_model=Dokument)
def read_dokument(document_id: int):
    if document_id not in dokument_db:
        raise HTTPException(status_code=404, detail="Dokument nicht gefunden")
    return dokument_db[document_id]

@router.put("/{document_id}", response_model=Dokument)
def update_dokument(document_id: int, dokument: DokumentCreate):
    if document_id not in dokument_db:
        raise HTTPException(status_code=404, detail="Dokument nicht gefunden")
    updated = dokument.dict()
    updated['document_id'] = document_id
    updated['erstellungsdatum'] = dokument_db[document_id]['erstellungsdatum']  
    dokument_db[document_id] = updated
    return updated

@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dokument(document_id: int):
    if document_id not in dokument_db:
        raise HTTPException(status_code=404, detail="Dokument nicht gefunden")
    del dokument_db[document_id]
    return
