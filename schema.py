from pydantic import BaseModel
from typing import Optional

# Base schema for shared fields
class BookBase(BaseModel):
    title: str
    author: str
    published_year: int

# Schema for creating a book
class BookCreate(BookBase):
    pass

# Schema for updating a book
class BookUpdate(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None

# Schema for output (includes id)
class Book(BookBase):
    id: int

    class Config:
        orm_mode = True  # For Pydantic V1