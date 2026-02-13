# FastAPI REST API Service

A REST API service built with FastAPI and PostgreSQL featuring customer, supplier, product, order, and payment management.

## Features

- FastAPI framework with async support
- PostgreSQL database with SQLAlchemy ORM
- UUID primary keys
- Pydantic models for validation
- Clean architecture (models, schemas, routers, services)
- Alembic database migrations
- Proper error handling
- Email validation
- Logging support

## Project Structure

```
app/
├── main.py              # FastAPI application
├── database.py          # Database connection
├── config.py            # Configuration
├── dependencies.py      # Dependency injection
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas
├── routers/             # API endpoints
└── services/            # Business logic
alembic/                 # Database migrations
requirements.txt         # Dependencies
.env.example            # Environment variables template
```

## Setup

1. **Clone and navigate to project:**
```bash
cd TESTPYTHON
```

2. **Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your PostgreSQL credentials
```

5. **Create database migrations:**
```bash
alembic revision --autogenerate -m "Initial migration"
```

6. **Run migrations:**
```bash
alembic upgrade head
```

7. **Start the server:**
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Customer
- `POST /customer` - Create customer
- `GET /customer` - Get all customers
- `GET /customer/{id}` - Get customer by ID
- `PUT /customer/{id}` - Update customer
- `DELETE /customer/{id}` - Delete customer

### Supplier
- `POST /supplier` - Create supplier
- `GET /supplier` - Get all suppliers
- `GET /supplier/{id}` - Get supplier by ID
- `PUT /supplier/{id}` - Update supplier
- `DELETE /supplier/{id}` - Delete supplier

### Product
- `POST /product` - Create product
- `GET /product` - Get all products
- `GET /product/{id}` - Get product by ID
- `PUT /product/{id}` - Update product
- `DELETE /product/{id}` - Delete product

### Order
- `POST /order` - Create order
- `GET /order` - Get all orders
- `GET /order/{id}` - Get order by ID
- `PUT /order/{id}` - Update order
- `DELETE /order/{id}` - Delete order

### Payment
- `POST /payment` - Create payment
- `GET /payment` - Get all payments
- `GET /payment/{id}` - Get payment by ID
- `PUT /payment/{id}` - Update payment
- `DELETE /payment/{id}` - Delete payment

## Database Schema

### Relationships
- One Supplier → Many Products
- One Customer → Many Orders
- One Order → One Payment

### Enums
- **OrderStatus**: Pending, Shipped, Delivered, Cancelled
- **PaymentMethod**: Card, UPI, Cash, Bank Transfer
- **PaymentStatus**: Pending, Completed, Failed

## Example Usage

### Create a Customer
```bash
curl -X POST "http://localhost:8000/customer" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "1234567890",
    "address": "123 Main St"
  }'
```

### Create a Supplier
```bash
curl -X POST "http://localhost:8000/supplier" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "ABC Supplies",
    "email": "abc@example.com",
    "phone": "9876543210",
    "address": "456 Supply Ave"
  }'
```

### Create a Product
```bash
curl -X POST "http://localhost:8000/product" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Widget",
    "description": "A useful widget",
    "price": 29.99,
    "stock_quantity": 100,
    "supplier_id": "<supplier-uuid>"
  }'
```

## Database Migrations

### Create a new migration:
```bash
alembic revision --autogenerate -m "Description of changes"
```

### Apply migrations:
```bash
alembic upgrade head
```

### Rollback migration:
```bash
alembic downgrade -1
```

## Environment Variables

Required in `.env` file:
- `DATABASE_URL` - PostgreSQL connection string (format: `postgresql+asyncpg://user:password@host:port/database`)
