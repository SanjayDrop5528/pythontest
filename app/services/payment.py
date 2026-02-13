from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate, PaymentUpdate

class PaymentService:
    @staticmethod
    async def create(db: AsyncSession, payment: PaymentCreate) -> Payment:
        db_payment = Payment(**payment.model_dump())
        db.add(db_payment)
        await db.commit()
        await db.refresh(db_payment)
        return db_payment
    
    @staticmethod
    async def get_all(db: AsyncSession) -> list[Payment]:
        result = await db.execute(select(Payment))
        return result.scalars().all()
    
    @staticmethod
    async def get_by_id(db: AsyncSession, payment_id: UUID) -> Payment | None:
        result = await db.execute(select(Payment).where(Payment.id == payment_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def update(db: AsyncSession, payment_id: UUID, payment: PaymentUpdate) -> Payment | None:
        db_payment = await PaymentService.get_by_id(db, payment_id)
        if not db_payment:
            return None
        for key, value in payment.model_dump().items():
            setattr(db_payment, key, value)
        await db.commit()
        await db.refresh(db_payment)
        return db_payment
    
    @staticmethod
    async def delete(db: AsyncSession, payment_id: UUID) -> bool:
        db_payment = await PaymentService.get_by_id(db, payment_id)
        if not db_payment:
            return False
        await db.delete(db_payment)
        await db.commit()
        return True
