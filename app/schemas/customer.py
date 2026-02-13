from pydantic import BaseModel, EmailStr, ConfigDict
from uuid import UUID
from datetime import datetime

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: UUID
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
