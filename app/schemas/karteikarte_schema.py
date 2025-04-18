from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class KarteikarteBase(BaseModel):
    frage: str
    antwort: str
    kategorie: str
    dokument_id: Optional[int] = None   
    topic_id: Optional[int] = None      
    kurs_id: Optional[int] = None       

class KarteikarteCreate(KarteikarteBase):
    pass

class Karteikarte(KarteikarteBase):
    kartei_id: int
    erstellungsdatum: datetime

    class Config:
        orm_mode = True
