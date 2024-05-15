from fastapi import APIRouter


router = APIRouter(tags=["Auth"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
