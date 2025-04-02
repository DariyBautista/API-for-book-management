from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.auth.services import register_user, login_user
from app.schemas.schemas import UserCreate, UserLogin,UserResponse ,Token
from app.database.connection import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
async def register_user_view(user_data: UserCreate, db: Session = Depends(get_db)):
    return await register_user(user_data, db)

@router.post("/login", response_model=Token)
async def login_view(data: UserLogin, db: Session = Depends(get_db)):
    return await login_user(data, db)
