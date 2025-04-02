from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.models import Book, User, UserRole
from app.schemas.schemas import BookCreate, BookUpdate
from app.auth.services import check_role


async def create_book(book_data: BookCreate, db: Session, current_user: User):
    if current_user.role not in [UserRole.writer, UserRole.admin]:
        raise HTTPException(status_code=403, detail="Permission denied.")
    
    new_book = Book(**book_data.dict(), owner_id=current_user.id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

async def get_books(db: Session):
    return db.query(Book).all()

async def get_book(book_id: int, db: Session):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

async def update_book(book_id: int, book_data: BookUpdate, db: Session, current_user: User):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if book.owner_id != current_user.id and current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Access denied")
    
    for key, value in book_data.dict().items():
        setattr(book, key, value)
    
    db.commit()
    db.refresh(book)
    return book

async def delete_book(book_id: int, db: Session, current_user: User):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if book.owner_id != current_user.id and current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Access denied")
    
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}
