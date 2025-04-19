from pydantic import BaseModel, EmailStr

class AutorBase(BaseModel):
    name: str
    email: EmailStr

class AutorCreate(AutorBase):
    pass

class Autor(AutorBase):
    autor_id: str

    class Config:
        orm_mode = True
