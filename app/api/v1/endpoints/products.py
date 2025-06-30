from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.product import ProductCreate, ProductUpdate, Product
from app.crud.product_crud import (
    get_product,
    get_products,
    create_product,
    update_product,
    delete_product
)

router = APIRouter()

@router.get("/products", response_model=List[Product])
async def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products(db, skip=skip, limit=limit)
    return products

@router.post("/products", response_model=Product)
async def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = create_product(db, product)
    return db_product

@router.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/products/{product_id}", response_model=Product)
async def update_existing_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = update_product(db, product_id, product)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.delete("/products/{product_id}", response_model=Product)
async def delete_product(product_id:int, db:Session = Depends(get_db)):
    db_product = delete_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product