from pydantic import BaseModel, EmailStr
from typing import List, Optional
from enum import Enum
from datetime import date

class UserRole(str, Enum):
    admin = "admin"
    writer = "writer"
    reader = "reader"
    
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.reader

class UserRoleUpdate(BaseModel):
    role: UserRole

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: UserRole
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    published_date: Optional[date] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    owner_id: int
    
    class Config:
        from_attributes = True


