# insidersTestFastAPItask

# 📚 API для управління книгами

## 🔥 Опис проекту

Даний API реалізує систему управління книгами з авторизацією, ролями користувачів та CRUD-операціями для книг.

### 🎯 Функціонал:

#### 1️⃣ Авторизація та реєстрація
- Реалізовано механізм авторизації та реєстрації користувачів.
- Використовується JWT (JSON Web Tokens) для захисту маршрутів та управління сеансами користувачів.

#### 2️⃣ RBAC (Role-Based Access Control)
- Впроваджено три ролі:
  - **Читач**: має доступ тільки до перегляду книг.
  - **Письменник**: може створювати та редагувати та видаляти свої книги.
  - **Адміністратор**: має повний контроль над книгами та управління ролями користувачів.

#### 3️⃣ CRUD для книг
- Створення, перегляд, редагування та видалення книг:
  - Додавання книги.
  - Перегляд списку книг.
  - Редагування інформації про книги.
  - Видалення книг.

---

## 🛠 Технологічний стек

- **FastAPI** – для побудови бекенду.
- **SQLAlchemy** – ORM для роботи з базою даних.
- **Alembic** – для управління міграціями бази даних.
- **PostgreSQL** – основна база даних.

---

## 🚀 Запуск проекту

1. Встановлення залежностей:
   ```bash
   pip install -r requirements.txt
   ```

2. Ініціалізація alembic:
   ```bash
   alembic init alembic
   ```
3. Налаштування alembic.ini  
   змінити під свою базу даних
   ```bash
   sqlalchemy.url = postgresql://username:password@localhost/DBname
   ```
4. Оновлюємо alembic/env.py
   ```bash
   from app.models import Base  
   from app.database import DATABASE_URL  

   config.set_main_option("sqlalchemy.url", DATABASE_URL)  
   target_metadata = Base.metadata  
   ```
5. Створення та застосування міграцій
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```
   ```bash
   alembic upgrade head
   ```
6. Запуск сервера:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 🔗 Ендпойнти API

### 🔐 Авторизація

#### Реєстрація користувача
**POST** `/auth/register`

📌 **Запит:**
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepassword",
  "role": "reader"
}
```

✅ **Відповідь:**
```json
{
  "id": 1,
  "username": "testuser",
  "email": "test@example.com",
  "role": "reader"
}
```

#### Логін користувача
**POST** `/auth/login`

📌 **Запит:**
```json
{
  "username": "admin",
  "password": "your_password"
}
```

✅ **Відповідь:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

⚠️ Для подальшого доступу необхідно передавати JWT токен у заголовку у форматі:
```
'Authorization': 'Bearer <JWT_TOKEN>'
```

---

### 📚 Управління книгами

#### Створення книги
**POST** `/books/`

📌 **Запит:**
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "description": "A novel set in the Roaring Twenties.",
  "published_date": "1925-04-10"
}
```

✅ **Відповідь:**
```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "description": "A novel set in the Roaring Twenties.",
  "published_date": "1925-04-10",
  "owner_id": 1
}
```

#### Отримання списку книг
**GET** `/books/`

📌 **Запит:** (JWT токен у заголовку )

✅ **Відповідь:**
```json
[
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "description": "A novel set in the Roaring Twenties.",
    "published_date": "1925-04-10"
  }
]
```

#### Отримання конкретної книги
**GET** `/books/{book_id}`

📌 **Запит:** (JWT токен у заголовку)

#### Оновлення книги
**PUT** `/books/{book_id}`

📌 **Запит:** (JWT токен у заголовку)
```json
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "description": "A novel set in the Roaring Twenties.",
  "published_date": "2002-06-06"
}
```

#### Видалення книги
**DELETE** `/books/{book_id}`

📌 **Запит:** (JWT токен у заголовку)

---

### 👤 Управління користувачами (для ролі **Адміністратор**)

#### Отримання всіх користувачів
**GET** `/users/`

📌 **Запит:** (JWT токен **адміністратора** у заголовку)

#### Оновлення ролі користувача
**PUT** `/users/{user_id}/role`

📌 📌 **Запит:** (JWT токен **адміністратора** у заголовку)
```json
{
  "role": "writer"
}
```

#### Видалення користувача
**DELETE** `/users/{user_id}`

📌 **Запит:** (JWT токен **адміністратора** у заголовку)

---

**Проект повністю готовий до використання!**


