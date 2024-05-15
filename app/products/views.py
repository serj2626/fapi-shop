from fastapi import APIRouter, HTTPException
from .crud import ProductCRUD, CategoryCRUD


router = APIRouter(tags=["Продукты"])


@router.get("/")
async def get_all_products():
    products = await ProductCRUD.find_all()
    return products


@router.get("/{product_id}")
async def get_product(product_id: int):
    product = await ProductCRUD.find_one_or_none(id=product_id)
    if product is not None:
        return product
    raise HTTPException(status_code=404, detail="Продукт не найден")


@router.get("/categories")
async def get_all_categories():
    categories = await CategoryCRUD.find_all()
    return categories


@router.get("/categories/{category_id}")
async def get_category(category_id: int):
    category = await CategoryCRUD.find_one_or_none(id=category_id)
    if category is not None:
        return category
    raise HTTPException(status_code=404, detail="Категория не найдена")
