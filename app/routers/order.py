from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from app.services.order import OrderService
from app.dependencies import get_db

router = APIRouter(prefix="/order", tags=["orders"])

@router.post("", response_model=OrderResponse)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    return await OrderService.create(db, order)

@router.get("", response_model=list[OrderResponse])
async def get_orders(db: AsyncSession = Depends(get_db)):
    return await OrderService.get_all(db)

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: UUID, db: AsyncSession = Depends(get_db)):
    order = await OrderService.get_by_id(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(order_id: UUID, order: OrderUpdate, db: AsyncSession = Depends(get_db)):
    updated = await OrderService.update(db, order_id, order)
    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated

@router.delete("/{order_id}")
async def delete_order(order_id: UUID, db: AsyncSession = Depends(get_db)):
    deleted = await OrderService.delete(db, order_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted"}
