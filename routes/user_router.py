from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from config.database import get_db
from models.schemas import UserInput, UserRegister
from services.auth_service import JWTBearer
from services.user_service import UserService
from sqlalchemy.orm import Session

user_router = APIRouter(tags=["User"], dependencies=[Depends(JWTBearer())])

user_Service = UserService()


def get_current_user(token: str) -> dict | None:
    try:
        # if not token:
        #     raise HTTPException(status_code=401, detail="No token provided")
        # user = auth.verify_id_token(token.credentials)
        # print(user)
        user = "1234"
        return user

    except Exception as exc:
        raise HTTPException(status_code=401, detail="Invalid credentials") from exc


@user_router.get("/users/me")
async def get_user_id(user: Annotated[dict, Depends(get_current_user)]):
    return {"userId": user}


@user_router.get("/users/{userId}/brands", tags=["User"])
def get_all_user_brand(userId: str, db: Session = Depends(get_db)):
    return user_Service.get_user_brands(userId, db=db)


@user_router.get("/users/me")
def get_user_details(userId: str, db: Session = Depends(get_db)):
    data = user_Service.get_user(userId, db)
    return JSONResponse(content={"message": "Fetched users data", "data": data})


@user_router.patch("/users/{userId}")
def update_user_details(userId: str, data: UserRegister, db: Session = Depends(get_db)):
    data = user_Service.update_user(userId, data, db)
    return JSONResponse(content={"message": "Updated users data", "data": data})
