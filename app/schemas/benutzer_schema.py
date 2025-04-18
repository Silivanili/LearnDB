from pydantic import BaseModel, EmailStr

class BenutzerBase(BaseModel):
    name: str
    email: EmailStr

class BenutzerCreate(BenutzerBase):
    pass

class Benutzer(BenutzerBase):
    benutzer_id: str

    class Config:
        orm_mode = True
