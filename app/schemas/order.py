from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from decimal import Decimal
from app.models.order import OrderStatus

class OrderBase(BaseModel):
    customer_id: UUID
    status: OrderStatus
    total_amount: Decimal

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: UUID
    order_date: datetime
    
    model_config = ConfigDict(from_attributes=True)
