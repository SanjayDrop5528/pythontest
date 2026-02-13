from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

class ProductService:
    @staticmethod
    async def create(db: AsyncSession, product: ProductCreate) -> Product:
        db_product = Product(**product.model_dump())
        db.add(db_product)
        await db.commit()
        await db.refresh(db_product)
        return db_product
    
    @staticmethod
    async def get_all(db: AsyncSession) -> list[Product]:
        result = await db.execute(select(Product))
        return result.scalars().all()
    
    @staticmethod
    async def get_by_id(db: AsyncSession, product_id: UUID) -> Product | None:
        result = await db.execute(select(Product).where(Product.id == product_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def update(db: AsyncSession, product_id: UUID, product: ProductUpdate) -> Product | None:
        db_product = await ProductService.get_by_id(db, product_id)
        if not db_product:
            return None
        for key, value in product.model_dump().items():
            setattr(db_product, key, value)
        await db.commit()
        await db.refresh(db_product)
        return db_product
    
    @staticmethod
    async def delete(db: AsyncSession, product_id: UUID) -> bool:
        db_product = await ProductService.get_by_id(db, product_id)
        if not db_product:
            return False
        await db.delete(db_product)
        await db.commit()
        return True
