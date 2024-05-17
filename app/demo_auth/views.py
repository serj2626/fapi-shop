from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from typing import Annotated
import secrets

router = APIRouter(tags=["Demo-Auth"])

security = HTTPBasic()


# Базовая Аутентификация
@router.get("/basic-auth")
async def demo_auth(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}


username_to_passwords = {
    "admin": "admin",
    "user": "user",
}


def get_auth_user_username(data: Annotated[HTTPBasicCredentials, Depends(security)]):
    unauthed_exc = HTTPException(
        status_code=401,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    correct_psw = username_to_passwords.get(data.username)

    if correct_psw is None:
        raise unauthed_exc
    if not secrets.compare_digest(
        data.password.encode("utf-8"), correct_psw.encode("utf-8")
    ):
        raise unauthed_exc
    return data.username


@router.get("/check-basic-auth")
async def check_basic_auth(auth_username: str = Depends(get_auth_user_username)):
    return {"username": auth_username}
