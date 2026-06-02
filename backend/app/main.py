from fastapi import FastAPI

from app.database import engine
from app import models
from app.routes.products import router as product_router
from app.routes.customers import router as customer_router
from app.routes.orders import router as order_router
from fastapi.middleware.cors import CORSMiddleware
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(product_router)
app.include_router(customer_router)
app.include_router(order_router)


@app.get("/")
def home():
    return {
        "message": "Inventory & Order Management System"
    }