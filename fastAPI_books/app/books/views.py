from fastapi import APIRouter, HTTPException, Depends
from app.books.services import create_book, get_books, get_book, update_book, delete_book
from app.schemas.schemas import BookCreate, BookUpdate, BookResponse
from app.database.connection import get_db
from app.auth.services import get_current_user
from app.models.models import UserRole, User
from sqlalchemy.orm import Session

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=BookResponse)
async def create_book_view(
    book_data: BookCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return await create_book(book_data, db, current_user)

@router.get("/", response_model=list[BookResponse])
async def get_books_view(db: Session = Depends(get_db)):
    return await get_books(db)

@router.get("/{book_id}", response_model=BookResponse)
async def get_book_view(book_id: int, db: Session = Depends(get_db)):
    return await get_book(book_id, db)

@router.put("/{book_id}", response_model=BookResponse)
async def update_book_view(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await update_book(book_id, book_data, db, current_user)

@router.delete("/{book_id}")
async def delete_book_view(book_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return await delete_book(book_id, db, current_user)
