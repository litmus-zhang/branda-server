from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from firebase_admin import auth
from firebase_admin.auth import UserRecord
from typing import Annotated
from dotenv import load_dotenv
from config.helper import BrandService
from models.schemas import Strategy, Base, BaseBody, UserInput
from config.firebase import init_firebase
from passlib.hash import argon2 as argon



load_dotenv()

db, _auth = init_firebase()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")  # Placeholder for login endpoint

brand_service = BrandService()

router = APIRouter()
@router.get("/status", tags=["Health check"])
async def get_status():
    return {
        "message": "All system operational",
        "status": "OK"
    }

@router.get("/font", tags=["Brand"])
async def get_font():
    data = brand_service.get_font()
    return JSONResponse(content={
        "message": "Font Received Successfully",
        "data": data
    })


@router.post("/{userId}/brands/{brandId}/font", tags=["Brand"])
async def create_font(base: BaseBody, userId: str, brandId:str):
    # store in db
    pass


@router.get("/color", tags=["Brand"])
async def get_color_pallete(base: Base):
    data = brand_service.get_color_pallete(base)
    return JSONResponse(content={
        "message": "Color pallete received successfully",
        "data": data
    })

@router.post("/{userId}/brands/{brandId}/color", tags=["Brand"])
async def create_color_pallete(base: BaseBody, userId: str, brandId: str):
    # store in db
    pass


@router.get("/messaging", tags=["Brand"])
def get_brand_messaging(base: Base):
    data = brand_service.get_brand_messaging(base)
    return JSONResponse(content={
        "message": "Brand messaging received Successfully",
        "data": data
    })

@router.post("/{userId}/brands/{brandId}/messaging", tags=["Brand"])
def create_brand_messaging(base: BaseBody, userId: str, brandId: str):
    # store in db
    pass

@router.get("/strategy", tags=["Brand"])
def get_brand_strategy(brand_strategy: Strategy):
    data = brand_service.get_brand_strategy(brand_strategy)
    return JSONResponse(content={
        "message": "Brand strategy received successfully",
        "data": data
    })

@router.post("/{userId}/brands/{brandId}", tags=["Brand"])
def create_brand_strategy(brand_strategy: BaseBody, userId: str, brandId: str):
    # store in db
    pass

@router.get("/brand_name", tags=["Brand"])
def get_brand_name(base: Base):
    data = brand_service.get_brand_name(base)
    return JSONResponse(content={
        "message": "Brand names fetched successfully",
        "data": data
    })

@router.post("/{userId}/brands/{brandId}", tags=["Brand"], status_code=201)
def post_brand_name(base: BaseBody, userId: str, brandId: str):
    # store in db
    pass


@router.get("/logo", tags=["Brand"])
def get_logo(base: Base):
    return brand_service.get_logo(base)

@router.post("/{userId}/brands/{brandId}/logo", tags=["Brand"])
def create_logo(base: BaseBody, userId: str, brandId: str):
    # store in db
    pass

@router.get("/photography", tags=["Brand"])
def get_photography(base: Base):
    return brand_service.get_photography(base)

@router.post("{userId}/brands/{brandId}/photography", tags=["Brand"])
def create_photography(base: BaseBody, userId: str, brandId: str):
    # store in db
    pass

@router.get("/illustration", tags=["Brand"])
def get_illustration(base: Base):
    return brand_service.get_illustration(base)

@router.post("{userId}/brands/{brandId}/illustration", tags=["Brand"])
def create_illustration(base: BaseBody, userId: str, brandId: str):
    # store in db
    pass

@router.get("/{userId}/brands", tags=["Brand"])
def get_all_user_brand(userId: str):
    data = ""
    return JSONResponse(content={
        "message": "All user brand",
        "data": data
    })

@router.get("/users/me", tags=["Brand"])
def get_user_details(userId: str):
    data = auth.get_user(userId)
    return JSONResponse(content={
        "message": "Fetched users data",
        "data": data
    })


@router.post("/login", tags=['Authentication'])
async def login(user: UserInput) :
    try:
        s = auth.get_user_by_email(user.email)
        if  s == auth.UserNotFoundError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
        return JSONResponse(content={
            "message": "User login successful"
        }
        )
    except Exception as exc:
        raise HTTPException(status_code=401, detail="Invalid Google access token") from exc


@router.post("/signup", tags=['Authentication'])
async def signup(user: UserInput):
    try:
        if auth.get_user_by_email(user.email) is not UserRecord:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exist")
        auth.create_user(email=user.email, password=user.password)
        return JSONResponse(content={
            "message": "User registration successful"})
    except HTTPException as exc :
        raise HTTPException(detail="Invalid credentials", status_code=status.HTTP_400_BAD_REQUEST) from exc