from pydantic import BaseModel

class TopicBase(BaseModel):
    name: str
    beschreibung: str

class TopicCreate(TopicBase):
    pass

class Topic(TopicBase):
    topic_id: str

    class Config:
        orm_mode = True
