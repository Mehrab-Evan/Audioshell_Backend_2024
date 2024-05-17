from pydantic import BaseModel

class UserBase(BaseModel):
    pass

class UserCreate(UserBase):
    username: str
    email: str
    password: str

class UserLogin(UserBase):
    username: str
    password: str
