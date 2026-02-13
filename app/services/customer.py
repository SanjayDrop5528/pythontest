from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate

class CustomerService:
    @staticmethod
    async def create(db: AsyncSession, customer: CustomerCreate) -> Customer:
        db_customer = Customer(**customer.model_dump())
        db.add(db_customer)
        await db.commit()
        await db.refresh(db_customer)
        return db_customer
    
    @staticmethod
    async def get_all(db: AsyncSession) -> list[Customer]:
        result = await db.execute(select(Customer))
        return result.scalars().all()
    
    @staticmethod
    async def get_by_id(db: AsyncSession, customer_id: UUID) -> Customer | None:
        result = await db.execute(select(Customer).where(Customer.id == customer_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def update(db: AsyncSession, customer_id: UUID, customer: CustomerUpdate) -> Customer | None:
        db_customer = await CustomerService.get_by_id(db, customer_id)
        if not db_customer:
            return None
        for key, value in customer.model_dump().items():
            setattr(db_customer, key, value)
        await db.commit()
        await db.refresh(db_customer)
        return db_customer
    
    @staticmethod
    async def delete(db: AsyncSession, customer_id: UUID) -> bool:
        db_customer = await CustomerService.get_by_id(db, customer_id)
        if not db_customer:
            return False
        await db.delete(db_customer)
        await db.commit()
        return True
