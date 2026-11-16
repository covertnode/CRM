from fastapi import FastAPI, HTTPException
from app.routers.health import router as health_router
from app.routers.customers import router as customers_router

app = FastAPI()

app.include_router(health_router)
app.include_router(customers_router)

@app.get("/")
def home():
    return {"message": "Welcome to the AI CRM!"}


@app.get("/products/123")
def get_product():
    raise HTTPException(
        status_code=404,
        detail="Product not found."
    )
