from fastapi import APIRouter, HTTPException, status
from typing import Dict
from schemas.topic_schema import Topic, TopicCreate

router = APIRouter()

topic_db: Dict[int, dict] = {}
next_id = 1

@router.post("/", response_model=Topic, status_code=status.HTTP_201_CREATED)
def create_topic(topic: TopicCreate):
    global next_id
    new_topic = topic.dict()
    new_topic['topic_id'] = next_id
    topic_db[next_id] = new_topic
    next_id += 1
    return new_topic

@router.get("/{topic_id}", response_model=Topic)
def read_topic(topic_id: int):
    if topic_id not in topic_db:
        raise HTTPException(status_code=404, detail="Topic nicht gefunden")
    return topic_db[topic_id]

@router.put("/{topic_id}", response_model=Topic)
def update_topic(topic_id: int, topic: TopicCreate):
    if topic_id not in topic_db:
        raise HTTPException(status_code=404, detail="Topic nicht gefunden")
    updated = topic.dict()
    updated['topic_id'] = topic_id
    topic_db[topic_id] = updated
    return updated

@router.delete("/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_topic(topic_id: int):
    if topic_id not in topic_db:
        raise HTTPException(status_code=404, detail="Topic nicht gefunden")
    del topic_db[topic_id]
    return
