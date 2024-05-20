from fastapi import FastAPI
from app.auth import auth_router
from app.products import products_router
from app.demo_auth import demo_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(products_router, prefix="/products")
# app.include_router(demo_router, prefix="/demo")
