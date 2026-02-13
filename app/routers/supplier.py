from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.schemas.supplier import SupplierCreate, SupplierUpdate, SupplierResponse
from app.services.supplier import SupplierService
from app.dependencies import get_db

router = APIRouter(prefix="/supplier", tags=["suppliers"])

@router.post("", response_model=SupplierResponse)
async def create_supplier(supplier: SupplierCreate, db: AsyncSession = Depends(get_db)):
    return await SupplierService.create(db, supplier)

@router.get("", response_model=list[SupplierResponse])
async def get_suppliers(db: AsyncSession = Depends(get_db)):
    return await SupplierService.get_all(db)

@router.get("/{supplier_id}", response_model=SupplierResponse)
async def get_supplier(supplier_id: UUID, db: AsyncSession = Depends(get_db)):
    supplier = await SupplierService.get_by_id(db, supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier

@router.put("/{supplier_id}", response_model=SupplierResponse)
async def update_supplier(supplier_id: UUID, supplier: SupplierUpdate, db: AsyncSession = Depends(get_db)):
    updated = await SupplierService.update(db, supplier_id, supplier)
    if not updated:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return updated

@router.delete("/{supplier_id}")
async def delete_supplier(supplier_id: UUID, db: AsyncSession = Depends(get_db)):
    deleted = await SupplierService.delete(db, supplier_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return {"message": "Supplier deleted"}
