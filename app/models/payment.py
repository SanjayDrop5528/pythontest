from sqlalchemy import Column, DateTime, Numeric, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum
from app.database import Base

class PaymentMethod(str, enum.Enum):
    CARD = "Card"
    UPI = "UPI"
    CASH = "Cash"
    BANK_TRANSFER = "Bank Transfer"

class PaymentStatus(str, enum.Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"

class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"), nullable=False, unique=True, index=True)
    payment_date = Column(DateTime(timezone=True), server_default=func.now())
    amount = Column(Numeric(10, 2), nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.PENDING)
    
    order = relationship("Order", back_populates="payment")
