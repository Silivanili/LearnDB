from datetime import datetime
from pydantic import BaseModel

class KursBase(BaseModel):
    name: str
    beschreibung: str
    ort: str
    sonstige_infos: str

class KursCreate(KursBase):
    pass

class Kurs(KursBase):
    kurs_id: str
    Zeit: datetime

    class Config:
        orm_mode = True
