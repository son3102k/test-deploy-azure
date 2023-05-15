from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserLogin(UserBase):
    password: str

class UserCreate(UserLogin):
    name: str

class UserInfo(UserBase):
    user_id: int
    name: str
    role: int

    class Config():
        orm_mode = True