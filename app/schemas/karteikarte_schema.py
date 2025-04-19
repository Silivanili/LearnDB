from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class KarteikarteBase(BaseModel):
    frage: str
    antwort: str
    kategorie: str
    dokument_id: Optional[str] = None   
    topic_id: Optional[str] = None      
    kurs_id: Optional[str] = None       

class KarteikarteCreate(KarteikarteBase):
    pass

class Karteikarte(KarteikarteBase):
    kartei_id: str
    erstellungsdatum: datetime

    class Config:
        orm_mode = True
