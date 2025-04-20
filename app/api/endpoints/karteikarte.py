from fastapi import APIRouter, HTTPException, status, Depends
from datetime import datetime
from bson import ObjectId
from pymongo import ReturnDocument
from schemas.karteikarte_schema import Karteikarte, KarteikarteCreate
from db.mongo import get_database

router = APIRouter()

@router.post("/", response_model=Karteikarte, status_code=status.HTTP_201_CREATED)
async def create_karteikarte(
    karteikarte: KarteikarteCreate,
    db=Depends(get_database)
):
    data = karteikarte.dict()
    data["erstellungsdatum"] = datetime.utcnow()
    result = await db.karteikarten.insert_one(data)                      
    created = await db.karteikarten.find_one({"_id": result.inserted_id})
    created["kartei_id"] = str(created.pop("_id"))
    print("created:", created)
    return created

@router.get("/{kartei_id}", response_model=Karteikarte)
async def read_karteikarte(
    kartei_id: str,
    db=Depends(get_database)
):
    record = await db.karteikarten.find_one({"_id": ObjectId(kartei_id)})
    if not record:
        raise HTTPException(status_code=404, detail="Karteikarte nicht gefunden")
    record["kartei_id"] = str(record.pop("_id"))
    return record

@router.put("/{kartei_id}", response_model=Karteikarte)
async def update_karteikarte(
    kartei_id: str,
    karteikarte: KarteikarteCreate,
    db=Depends(get_database)
):
    updated = karteikarte.dict()
    updated["erstellungsdatum"] = (await db.karteikarten.find_one(
        {"_id": ObjectId(kartei_id)}, {"erstellungsdatum": 1}
    ))["erstellungsdatum"]
    result = await db.karteikarten.find_one_and_replace(
        {"_id": ObjectId(kartei_id)},
        updated,
        return_document=ReturnDocument.AFTER
    )
    if not result:
        raise HTTPException(status_code=404, detail="Karteikarte nicht gefunden")
    result["kartei_id"] = str(result.pop("_id"))
    return result

@router.delete("/{kartei_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_karteikarte(
    kartei_id: str,
    db=Depends(get_database)
):
    delete_result = await db.karteikarten.delete_one({"_id": ObjectId(kartei_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Karteikarte nicht gefunden")
    return