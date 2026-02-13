from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class SupplierBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(SupplierBase):
    pass

class SupplierResponse(SupplierBase):
    id: UUID
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
