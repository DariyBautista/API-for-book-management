from fastapi import APIRouter, Depends, HTTPException
from app.users.services import get_users, update_user_role, delete_user
from app.schemas.schemas import UserRoleUpdate, UserResponse
from app.database.connection import get_db
from app.auth.services import get_current_user
from app.models.models import UserRole, User
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
async def get_users_view(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await get_users(db, current_user)

@router.put("/{user_id}/role", response_model=UserResponse)
async def update_user_role_view(user_id: int, role_data: UserRoleUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await update_user_role(user_id, role_data, db, current_user)

@router.delete("/{user_id}", response_model=dict)
async def delete_user_view(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await delete_user(user_id, db, current_user)
