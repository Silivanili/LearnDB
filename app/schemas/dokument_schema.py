from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class DokumentBase(BaseModel):
    titel: str
    beschreibung: str
    inhalt: str
    schlagworte: List[str]
    kurs: Optional[str] = None
    autor_id: Optional[int] = None          
    topic_ids: Optional[List[int]] = []      

class DokumentCreate(DokumentBase):
    pass

class Dokument(DokumentBase):
    document_id: int
    erstellungsdatum: datetime

    class Config:
        orm_mode = True
