from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from decimal import Decimal
from app.models.payment import PaymentMethod, PaymentStatus

class PaymentBase(BaseModel):
    order_id: UUID
    amount: Decimal
    payment_method: PaymentMethod
    status: PaymentStatus

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: UUID
    payment_date: datetime
    
    model_config = ConfigDict(from_attributes=True)
