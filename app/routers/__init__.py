from app.routers.customer import router as customer_router
from app.routers.supplier import router as supplier_router
from app.routers.product import router as product_router
from app.routers.order import router as order_router
from app.routers.payment import router as payment_router

__all__ = ["customer_router", "supplier_router", "product_router", "order_router", "payment_router"]
