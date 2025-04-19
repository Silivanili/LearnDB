from fastapi import APIRouter, HTTPException, status, Depends   
from datetime import datetime
from bson import ObjectId
from pymongo import ReturnDocument
from schemas.kurs_schema import Kurs, KursCreate
from db.mongo import get_database

router = APIRouter()

@router.post("/", response_model=Kurs, status_code=status.HTTP_201_CREATED)
async def create_kurs(
    kurs: KursCreate,
    db=Depends(get_database)
):
    data = kurs.dict()
    data["Zeit"] = datetime.utcnow()
    result = await db.courses.insert_one(data)                         
    created = await db.courses.find_one({"_id": result.inserted_id})
    created["kurs_id"] = str(created.pop("_id"))
    print("created:", created)
    return created

@router.get("/{kurs_id}", response_model=Kurs)
async def read_kurs(
    kurs_id: str,
    db=Depends(get_database)
):
    record = await db.courses.find_one({"_id": ObjectId(kurs_id)})
    if not record:
        raise HTTPException(status_code=404, detail="Kurs nicht gefunden")
    record["kurs_id"] = str(record.pop("_id"))
    return record

@router.put("/{kurs_id}", response_model=Kurs)
async def update_kurs(
    kurs_id: str,
    kurs: KursCreate,
    db=Depends(get_database)
):
    updated = kurs.dict()
    updated["Zeit"] = (await db.courses.find_one(
        {"_id": ObjectId(kurs_id)}, {"Zeit": 1}
    ))["Zeit"]
    result = await db.courses.find_one_and_replace(
        {"_id": ObjectId(kurs_id)},
        updated,
        return_document=ReturnDocument.AFTER
    )
    if not result:
        raise HTTPException(status_code=404, detail="Kurs nicht gefunden")
    result["kurs_id"] = str(result.pop("_id"))
    return result

@router.delete("/{kurs_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_kurs(
    kurs_id: str,
    db=Depends(get_database)
):
    delete_result = await db.courses.delete_one({"_id": ObjectId(kurs_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Kurs nicht gefunden")
    return
