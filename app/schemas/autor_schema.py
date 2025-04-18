from pydantic import BaseModel, EmailStr

class AutorBase(BaseModel):
    name: str
    email: EmailStr

class AutorCreate(AutorBase):
    pass

class Autor(AutorBase):
    autor_id: int

    class Config:
        orm_mode = True
