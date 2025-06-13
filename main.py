from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine, Base
from model import Book
from schema import Book, BookCreate, BookUpdate
from functions import create_book, get_book, get_books, update_book, delete_book
from database import get_db

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/books/", response_model=Book)
def create_book_endpoint(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.get("/books/", response_model=List[Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = get_books(db, skip, limit)
    return books

@app.put("/books/{book_id}", response_model=Book)
def update_book_endpoint(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = update_book(db, book_id, book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/{book_id}")
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    db_book = delete_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}