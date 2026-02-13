from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.schemas.payment import PaymentCreate, PaymentUpdate, PaymentResponse
from app.services.payment import PaymentService
from app.dependencies import get_db

router = APIRouter(prefix="/payment", tags=["payments"])

@router.post("", response_model=PaymentResponse)
async def create_payment(payment: PaymentCreate, db: AsyncSession = Depends(get_db)):
    return await PaymentService.create(db, payment)

@router.get("", response_model=list[PaymentResponse])
async def get_payments(db: AsyncSession = Depends(get_db)):
    return await PaymentService.get_all(db)

@router.get("/{payment_id}", response_model=PaymentResponse)
async def get_payment(payment_id: UUID, db: AsyncSession = Depends(get_db)):
    payment = await PaymentService.get_by_id(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.put("/{payment_id}", response_model=PaymentResponse)
async def update_payment(payment_id: UUID, payment: PaymentUpdate, db: AsyncSession = Depends(get_db)):
    updated = await PaymentService.update(db, payment_id, payment)
    if not updated:
        raise HTTPException(status_code=404, detail="Payment not found")
    return updated

@router.delete("/{payment_id}")
async def delete_payment(payment_id: UUID, db: AsyncSession = Depends(get_db)):
    deleted = await PaymentService.delete(db, payment_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"message": "Payment deleted"}
