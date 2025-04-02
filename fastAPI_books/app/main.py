from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.auth.views import router as auth_router
from app.books.views import router as books_router
from app.users.views import router as user_router
from app.database.connection import database

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(title="Books API", lifespan=lifespan)

app.include_router(auth_router)
app.include_router(books_router)
app.include_router(user_router)
