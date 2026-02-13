from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate

class OrderService:
    @staticmethod
    async def create(db: AsyncSession, order: OrderCreate) -> Order:
        db_order = Order(**order.model_dump())
        db.add(db_order)
        await db.commit()
        await db.refresh(db_order)
        return db_order
    
    @staticmethod
    async def get_all(db: AsyncSession) -> list[Order]:
        result = await db.execute(select(Order))
        return result.scalars().all()
    
    @staticmethod
    async def get_by_id(db: AsyncSession, order_id: UUID) -> Order | None:
        result = await db.execute(select(Order).where(Order.id == order_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def update(db: AsyncSession, order_id: UUID, order: OrderUpdate) -> Order | None:
        db_order = await OrderService.get_by_id(db, order_id)
        if not db_order:
            return None
        for key, value in order.model_dump().items():
            setattr(db_order, key, value)
        await db.commit()
        await db.refresh(db_order)
        return db_order
    
    @staticmethod
    async def delete(db: AsyncSession, order_id: UUID) -> bool:
        db_order = await OrderService.get_by_id(db, order_id)
        if not db_order:
            return False
        await db.delete(db_order)
        await db.commit()
        return True
