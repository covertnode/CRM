from fastapi import APIRouter

from app.schemas.customer import CustomerCreate

router = APIRouter(prefix="/api/v1/customers")

@router.get("/")
def get_customers():
    return {"customers": []}

@router.post("/")
def create_customer(customer: CustomerCreate):
    return customer
