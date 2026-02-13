from fastapi import FastAPI
import logging
from app.routers import customer_router, supplier_router, product_router, order_router, payment_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="REST API Service", version="1.0.0")

app.include_router(customer_router)
app.include_router(supplier_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(payment_router)

@app.get("/")
async def root():
    return {"message": "REST API Service"}

@app.on_event("startup")
async def startup_event():
    logger.info("Application started")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")
