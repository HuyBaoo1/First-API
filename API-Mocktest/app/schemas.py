from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

class MovieCreate(BaseModel):
    title: str
    year: int
    author: str

class MovieOut(BaseModel):
    id: int
    title: str
    year: int
    author: str

    class Config:
        orm_mode = True

class TVShowCreate(BaseModel):
    title: str
    year: int
    author: str

class TVShowOut(BaseModel):
    id: int
    title: str
    year: int
    author: str

    class Config:
        orm_mode = True

