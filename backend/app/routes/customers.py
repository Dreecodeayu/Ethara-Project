from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schema import CustomerCreate
from app.dependencies import get_db
from app import models

router = APIRouter()

customers = []

@router.post("/customers")
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):

    existing_customer = db.query(
        models.Customer
    ).filter(
        models.Customer.email == customer.email
    ).first()

    if existing_customer:
        return {
            "error": "Email already exists"
        }

    new_customer = models.Customer(
        name=customer.name,
        email=customer.email
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return {
        "message": "Customer created successfully",
        "id": new_customer.id
    }
@router.put("/customers/{email}")
def update_customer(
    email: str,
    updated_customer: CustomerCreate,
    db: Session = Depends(get_db)
):

    customer = db.query(
        models.Customer
    ).filter(
        models.Customer.email == email
    ).first()

    if not customer:
        return {
            "error": "Customer not found"
        }

    customer.name = updated_customer.name
    customer.email = updated_customer.email

    db.commit()

    return {
        "message": "Customer updated successfully"
    }

@router.delete("/customers/{email}")
def delete_customer(
    email: str,
    db: Session = Depends(get_db)
):

    customer = db.query(
        models.Customer
    ).filter(
        models.Customer.email == email
    ).first()

    if not customer:
        return {
            "error": "Customer not found"
        }

    db.delete(customer)
    db.commit()

    return {
        "message": "Customer deleted successfully"
    }
@router.get("/customers")
def get_customers(
    db: Session = Depends(get_db)
):

    customers = db.query(
        models.Customer
    ).all()

    return customers