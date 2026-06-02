from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schema import OrderCreate
from app.dependencies import get_db
from app import models

router = APIRouter()


@router.post("/orders")
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):

    customer = db.query(
        models.Customer
    ).filter(
        models.Customer.email == order.customer_email
    ).first()

    if not customer:
        return {
            "error": "Customer not found"
        }

    product = db.query(
        models.Product
    ).filter(
        models.Product.sku == order.product_sku
    ).first()

    if not product:
        return {
            "error": "Product not found"
        }

    if product.stock_quantity < order.quantity:
        return {
            "error": "Insufficient stock"
        }

    product.stock_quantity -= order.quantity

    new_order = models.Order(
        customer_id=customer.id,
        product_id=product.id,
        quantity=order.quantity
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {
        "message": "Order created successfully",
        "order_id": new_order.id,
        "remaining_stock": product.stock_quantity
    }


@router.get("/orders")
def get_orders(
    db: Session = Depends(get_db)
):

    orders = db.query(
        models.Order
    ).all()

    return orders