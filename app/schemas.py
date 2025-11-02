from pydantic import BaseModel

class SpecSourceBase(BaseModel):
   name: str
   email: str

class SpecSourceCreate(SpecSourceBase):
   pass

class SpecSourceObj(SpecSourceBase):   
    id: int
    class Config:
       orm_mode = True