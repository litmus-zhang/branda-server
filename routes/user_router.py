from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from models.schemas import UserInput
from services.auth_service import JWTBearer
from services.user_service import UserService

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


def check_user(data: UserInput):
    try:
        user = user_Service.get_user(data.email)
        if user:
            return JSONResponse(
                content={"message": "User received successfully", "data": "user"}
            )
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@user_router.get("/users/me")
async def get_user_id(user: Annotated[dict, Depends(get_current_user)]):
    return {"userId": user}


@user_router.get("/users/{userId}/brands", tags=["User"])
def get_all_user_brand(userId: str):
    return user_Service.get_user_brands(userId)


@user_router.get("/users/me")
def get_user_details(userId: str):
    data = "User data fetched successfully"
    return JSONResponse(content={"message": "Fetched users data", "data": data})
