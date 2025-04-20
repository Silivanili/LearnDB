from fastapi import APIRouter, HTTPException, status, Depends
from bson import ObjectId
from pymongo import ReturnDocument
from schemas.benutzer_schema import Benutzer, BenutzerCreate
from db.mongo import get_database

router = APIRouter()

@router.post("/", response_model=Benutzer, status_code=status.HTTP_201_CREATED)
async def create_benutzer(
    benutzer: BenutzerCreate,
    db=Depends(get_database)
):
    data = benutzer.dict()
    result = await db.benutzer.insert_one(data)                           
    created = await db.benutzer.find_one({"_id": result.inserted_id})
    created["benutzer_id"] = str(created.pop("_id"))
    print("created:", created)
    return created

@router.get("/{benutzer_id}", response_model=Benutzer)
async def read_benutzer(
    benutzer_id: str,
    db=Depends(get_database)
):
    record = await db.benutzer.find_one({"_id": ObjectId(benutzer_id)})
    if not record:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    record["benutzer_id"] = str(record.pop("_id"))
    return record

@router.put("/{benutzer_id}", response_model=Benutzer)
async def update_benutzer(
    benutzer_id: str,
    benutzer: BenutzerCreate,
    db=Depends(get_database)
):
    updated = benutzer.dict()
    result = await db.benutzer.find_one_and_replace(
        {"_id": ObjectId(benutzer_id)},
        updated,
        return_document=ReturnDocument.AFTER
    )
    if not result:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    result["benutzer_id"] = str(result.pop("_id"))
    return result

@router.delete("/{benutzer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_benutzer(
    benutzer_id: str,
    db=Depends(get_database)
):
    delete_result = await db.benutzer.delete_one({"_id": ObjectId(benutzer_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Benutzer nicht gefunden")
    return