from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from app.schemas.product import Product
from app.schemas.user import User


# OrderItem schema
class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    price_at_purchase: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemUpdate(OrderItemBase):
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    price_at_purchase: Optional[float] = None

class OrderItem(OrderItemBase):
    id: int

    class Config:
        orm_mode = True


# Order schema
class OrderBase(BaseModel):
    user_id: int
    total_amount: float

    class Config:
        orm_mode = True


class OrderCreate(OrderBase):
    order_items: List[OrderItemCreate]  # List of product IDs


class OrderUpdate(BaseModel):
    status: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: datetime
    status: str
    user: User
    items: List[OrderItem]

    class Config:
        orm_mode = True