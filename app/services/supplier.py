from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate, SupplierUpdate

class SupplierService:
    @staticmethod
    async def create(db: AsyncSession, supplier: SupplierCreate) -> Supplier:
        db_supplier = Supplier(**supplier.model_dump())
        db.add(db_supplier)
        await db.commit()
        await db.refresh(db_supplier)
        return db_supplier
    
    @staticmethod
    async def get_all(db: AsyncSession) -> list[Supplier]:
        result = await db.execute(select(Supplier))
        return result.scalars().all()
    
    @staticmethod
    async def get_by_id(db: AsyncSession, supplier_id: UUID) -> Supplier | None:
        result = await db.execute(select(Supplier).where(Supplier.id == supplier_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def update(db: AsyncSession, supplier_id: UUID, supplier: SupplierUpdate) -> Supplier | None:
        db_supplier = await SupplierService.get_by_id(db, supplier_id)
        if not db_supplier:
            return None
        for key, value in supplier.model_dump().items():
            setattr(db_supplier, key, value)
        await db.commit()
        await db.refresh(db_supplier)
        return db_supplier
    
    @staticmethod
    async def delete(db: AsyncSession, supplier_id: UUID) -> bool:
        db_supplier = await SupplierService.get_by_id(db, supplier_id)
        if not db_supplier:
            return False
        await db.delete(db_supplier)
        await db.commit()
        return True
