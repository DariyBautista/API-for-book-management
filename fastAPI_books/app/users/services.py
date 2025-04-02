from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.models import User, UserRole
from app.schemas.schemas import UserRoleUpdate


async def get_users(db: Session, current_user: User):
    if current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Access denied")
    return db.query(User).all()

async def update_user_role(user_id: int, role_data: UserRoleUpdate, db: Session, current_user: User):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Access denied")
    
    user.role = role_data.role
    db.commit()
    db.refresh(user)
    return user

async def delete_user(user_id: int, db: Session, current_user: User):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Access denied")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}
