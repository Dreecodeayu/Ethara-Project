from fastapi import APIRouter,Depends
from app.schema import ProductCreate
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app import models
from app.schema import ProductCreate
router = APIRouter()

products = []

@router.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    existing_product = db.query(
        models.Product
    ).filter(
        models.Product.sku == product.sku
    ).first()

    if existing_product:
        return {
            "error": "SKU already exists"
        }

    new_product = models.Product(
        name=product.name,
        sku=product.sku,
        price=product.price,
        stock_quantity=product.stock_quantity
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {
        "message": "Product created successfully",
        "id": new_product.id
    }
@router.get("/products")
def get_products(
    db: Session = Depends(get_db)
):

    products = db.query(
        models.Product
    ).all()

    return products

@router.put("/products/{sku}")
def update_product(
    sku: str,
    updated_product: ProductCreate,
    db: Session = Depends(get_db)
):

    product = db.query(
        models.Product
    ).filter(
        models.Product.sku == sku
    ).first()

    if not product:
        return {
            "error": "Product not found"
        }

    product.name = updated_product.name
    product.sku = updated_product.sku
    product.price = updated_product.price
    product.stock_quantity = updated_product.stock_quantity

    db.commit()

    return {
        "message": "Product updated successfully"
    }
@router.delete("/products/{sku}")
def delete_product(
    sku: str,
    db: Session = Depends(get_db)
):

    product = db.query(
        models.Product
    ).filter(
        models.Product.sku == sku
    ).first()

    if not product:
        return {
            "error": "Product not found"
        }

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }