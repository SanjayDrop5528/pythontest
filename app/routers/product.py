from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.services.product import ProductService
from app.dependencies import get_db

router = APIRouter(prefix="/product", tags=["products"])

@router.post("", response_model=ProductResponse)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    return await ProductService.create(db, product)

@router.get("", response_model=list[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)):
    return await ProductService.get_all(db)

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    product = await ProductService.get_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(product_id: UUID, product: ProductUpdate, db: AsyncSession = Depends(get_db)):
    updated = await ProductService.update(db, product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/{product_id}")
async def delete_product(product_id: UUID, db: AsyncSession = Depends(get_db)):
    deleted = await ProductService.delete(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted"}
