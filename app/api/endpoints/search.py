from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from bson import ObjectId
from db.mongo import get_database
from schemas.dokument_schema import Dokument

router = APIRouter()

@router.get("/", response_model=List[Dokument])
async def search_documents(
    query: str = Query(..., min_length=1),
    db=Depends(get_database)
):
    cursor = db.documents.find(         # Führt eine Textsuche in den Dokumenten durch.
        {"$text": {"$search": query}},
        {"score": {"$meta": "textScore"}}
    ).sort([("score", {"$meta": "textScore"})])
    results = []
    async for doc in cursor:
        doc["document_id"] = str(doc.pop("_id"))
        results.append(doc)
    if not results:
        raise HTTPException(status_code=404, detail="Keine Dokumente gefunden")
    return results
