from pydantic import BaseModel
from typing import Optional


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: Optional[str] = None
    description: Optional[str] = None


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

