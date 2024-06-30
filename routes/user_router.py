from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from config.database import get_db
from models.schemas import User, UserUpdate
from services.auth_handler import decode_jwt
from services.auth_service import JWTBearer
from services.user_service import UserService
from sqlalchemy.orm import Session

user_router = APIRouter(tags=["User"], dependencies=[Depends(JWTBearer())])

user_Service = UserService()


def get_current_user(
    user_id: str = Depends(JWTBearer()), db: Session = Depends(get_db)
) -> dict | None:
    userId = decode_jwt(user_id)
    return user_Service.get_user(userId["user_id"], db=db)


@user_router.get("/users/brands", tags=["User"])
def get_all_user_brand(
    user: Annotated[User, Depends(get_current_user)], db: Session = Depends(get_db)
):
    return user_Service.get_user_brands(user_id=user["id"], db=db)


@user_router.get("/users/me")
def get_user_details(user: Annotated[User, Depends(get_current_user)]):
    return JSONResponse(content={"message": "Fetched users data", "data": user})


@user_router.patch("/users/update")
def update_user_details(
    data: UserUpdate,
    user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    return user_Service.update_user(user["id"], data, db)
