from fastapi import APIRouter, HTTPException, status, Depends
from bson import ObjectId
from pymongo import ReturnDocument
from schemas.topic_schema import Topic, TopicCreate
from db.mongo import get_database

router = APIRouter()

@router.post("/", response_model=Topic, status_code=status.HTTP_201_CREATED)
async def create_topic(
    topic: TopicCreate,
    db=Depends(get_database)
):
    data = topic.dict()
    result = await db.topics.insert_one(data)                          
    created = await db.topics.find_one({"_id": result.inserted_id})
    created["topic_id"] = str(created.pop("_id"))
    print("created:", created)
    return created

@router.get("/{topic_id}", response_model=Topic)
async def read_topic(
    topic_id: str,
    db=Depends(get_database)
):
    record = await db.topics.find_one({"_id": ObjectId(topic_id)})
    if not record:
        raise HTTPException(status_code=404, detail="Topic nicht gefunden")
    record["topic_id"] = str(record.pop("_id"))
    return record

@router.put("/{topic_id}", response_model=Topic)
async def update_topic(
    topic_id: str,
    topic: TopicCreate,
    db=Depends(get_database)
):
    result = await db.topics.find_one_and_replace(
        {"_id": ObjectId(topic_id)},
        topic.dict(),
        return_document=ReturnDocument.AFTER
    )
    if not result:
        raise HTTPException(status_code=404, detail="Topic nicht gefunden")
    result["topic_id"] = str(result.pop("_id"))
    return result

@router.delete("/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_topic(
    topic_id: str,
    db=Depends(get_database)
):
    delete_result = await db.topics.delete_one({"_id": ObjectId(topic_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Topic nicht gefunden")
    return
