from app.service.service import BaseCRUD
from .models import Product, Category


class ProductCRUD(BaseCRUD):
    model = Product


class CategoryCRUD(BaseCRUD):
    model = Category