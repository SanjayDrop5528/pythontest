from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from decimal import Decimal

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    stock_quantity: int
    supplier_id: UUID

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: UUID
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
