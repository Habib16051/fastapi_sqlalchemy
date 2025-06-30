from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int
    category_id: int

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category_id: Optional[int] = None


class Product(ProductBase):
    id:int

    class Config:
        orm_mode = True
