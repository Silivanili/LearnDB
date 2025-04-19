from fastapi import APIRouter, HTTPException, status, Depends
from datetime import datetime
from bson import ObjectId
from schemas.dokument_schema import Dokument, DokumentCreate
from db.mongo import get_database

router = APIRouter()

@router.post("/", response_model=Dokument, status_code=status.HTTP_201_CREATED)
async def create_dokument(
    dokument: DokumentCreate,
    db=Depends(get_database)
):
    doc = dokument.dict()
    doc["erstellungsdatum"] = datetime.utcnow()
    result = await db.documents.insert_one(doc)     
    created = await db.documents.find_one({"_id": result.inserted_id})
    created["document_id"] = str(created.pop("_id"))
    print("created:", created)
    return created

@router.get("/{document_id}", response_model=Dokument)
async def read_dokument(
    document_id: str,
    db=Depends(get_database)
):
    record = await db.documents.find_one({"_id": ObjectId(document_id)})  
    if not record:
        raise HTTPException(status_code=404, detail="Dokument erstellt")
    record["document_id"] = str(record.pop("_id"))
    return record

@router.put("/{document_id}", response_model=Dokument)
async def update_dokument(
    document_id: str,
    dokument: DokumentCreate,
    db=Depends(get_database)
):
    updated_data = dokument.dict()
    updated_data["erstellungsdatum"] = (await db.documents.find_one(
        {"_id": ObjectId(document_id)}, {"erstellungsdatum": 1}
    ))["erstellungsdatum"]
    result = await db.documents.find_one_and_replace(
        {"_id": ObjectId(document_id)},
        updated_data,
        return_document=ReturnDocument.AFTER               
    )
    if not result:
        raise HTTPException(status_code=404, detail="Dokument erstellt")
    result["document_id"] = str(result.pop("_id"))
    return result

@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dokument(
    document_id: str,
    db=Depends(get_database)
):
    delete_result = await db.documents.delete_one({"_id": ObjectId(document_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Dokument nicht gefunden")
    return
