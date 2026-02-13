from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.schemas.customer import CustomerCreate, CustomerUpdate, CustomerResponse
from app.services.customer import CustomerService
from app.dependencies import get_db

router = APIRouter(prefix="/customer", tags=["customers"])

@router.post("", response_model=CustomerResponse)
async def create_customer(customer: CustomerCreate, db: AsyncSession = Depends(get_db)):
    return await CustomerService.create(db, customer)

@router.get("", response_model=list[CustomerResponse])
async def get_customers(db: AsyncSession = Depends(get_db)):
    return await CustomerService.get_all(db)

@router.get("/{customer_id}", response_model=CustomerResponse)
async def get_customer(customer_id: UUID, db: AsyncSession = Depends(get_db)):
    customer = await CustomerService.get_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=CustomerResponse)
async def update_customer(customer_id: UUID, customer: CustomerUpdate, db: AsyncSession = Depends(get_db)):
    updated = await CustomerService.update(db, customer_id, customer)
    if not updated:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated

@router.delete("/{customer_id}")
async def delete_customer(customer_id: UUID, db: AsyncSession = Depends(get_db)):
    deleted = await CustomerService.delete(db, customer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted"}
