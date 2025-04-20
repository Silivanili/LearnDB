from fastapi import APIRouter, HTTPException, status, Depends
from bson import ObjectId
from pymongo import ReturnDocument
from typing import Dict
from schemas.autor_schema import Autor, AutorCreate
from db.mongo import get_database

router = APIRouter()

@router.post("/", response_model=Autor, status_code=status.HTTP_201_CREATED)
async def create_autor(
    autor: AutorCreate,
    db=Depends(get_database)
):
    data = autor.dict()                             #Konvertiert Pydantic in ein normales Dict, weil MongoDB es sonst nicht handlen kann. Dann wird es gespeichert. Die ID muss konvertiert werden weil MongoDB diese so erwartet.                                          
    result = await db.autors.insert_one(data)                          
    created = await db.autors.find_one({"_id": result.inserted_id})
    created["autor_id"] = str(created.pop("_id"))
    print("created:", created)
    return created

@router.get("/{autor_id}", response_model=Autor)    #Verwendet find_one, um einzelnes Dokument anhand der ID abzurufen. Konvertiert den String autor_id in eine ObjectId zur Abfrage der Datenbank. Wandelt das Feld _id in autor_id um, um eine Antwort zu erhalten.
async def read_autor(
    autor_id: str,
    db=Depends(get_database)
):
    record = await db.autors.find_one({"_id": ObjectId(autor_id)})      
    if not record:
        raise HTTPException(status_code=404, detail="Autor nicht gefunden")
    record["autor_id"] = str(record.pop("_id"))
    return record

@router.put("/{autor_id}", response_model=Autor)    #Verwendet find_one_and_replace für die Aktualisierung. Wandelt das eingegebene Pydantic-Modell in ein Wörterbuch um. Wandelt die _id in der Antwort in autor_id um.
async def update_autor(
    autor_id: str,
    autor: AutorCreate,
    db=Depends(get_database)
):
    updated = autor.dict()
    result = await db.autors.find_one_and_replace(
        {"_id": ObjectId(autor_id)},
        updated,
        return_document=ReturnDocument.AFTER                              
    )
    if not result:
        raise HTTPException(status_code=404, detail="Autor nicht gefunden")
    result["autor_id"] = str(result.pop("_id"))
    return result

@router.delete("/{autor_id}", status_code=status.HTTP_204_NO_CONTENT)   #Verwendet delete_one, um ein Dokument zu löschen. Überprüft deleted_count, um sicherzustellen, dass ein Dokument gelöscht wurde. Gibt bei Erfolg eine leere Antwort (HTTP 204) zurück.
async def delete_autor(
    autor_id: str,
    db=Depends(get_database)
):
    delete_result = await db.autors.delete_one({"_id": ObjectId(autor_id)})  
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Autor nicht gefunden")
    return