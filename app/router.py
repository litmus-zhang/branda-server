from fastapi import APIRouter, Query, Depends, Body
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from restcountries import RestCountryApiV2 as rapi
import os
from typing import Annotated
from dotenv import load_dotenv
from config.helper import BrandService
from models.schemas import Strategy, Base, BaseBody, UserInput
import random
from config.firebase import init_firebase
from passlib.hash import argon2



load_dotenv()

db, auth = init_firebase()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")  # Placeholder for login endpoint

brand_service = BrandService

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


@router.post("{userId}/brands/{brandId}/font", tags=["Brand"])
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

@router.post("{userId}/brands/{brandId}/color", tags=["Brand"])
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

@router.post("{userId}/brands/{brandId}/messaging", tags=["Brand"])
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

@router.post("{userId}/brands/{brandId}", tags=["Brand"])
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

@router.post("{userId}/brands/{brandId}", tags=["Brand"], status_code=201)
def post_brand_name(base: BaseBody, userId: str, brandId: str):
    # store in db
    pass


@router.get("/logo", tags=["Brand"])
def get_logo(base: Base):
    return brand_service.get_logo(base)

@router.post("{userId}/brands/{brandId}/logo", tags=["Brand"])
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

@router.get("{userId}/brands", tags=["Brand"])
def get_all_user_brand(userId: str):
    data = db.collection(f'users/{userId}')
    return JSONResponse(content={
        "message": "All user brand",
        "data": data
    })


@router.get("/all-countries/", tags=["Extras"])
def get_all_countries(country_name: Annotated[str | None, Query(max_length=50)] = None ):
    all = rapi.get_all()
    countries = {}
    for country in all:
            countries[country.name] = {
                "name": country.name,
                "flag": country.flag
            }
    if country_name:
        return countries[country_name]
    else:
        return countries


@router.get("/login", tags=['Authentication'])
async def login(user) :
    try:
        decoded_token = auth.verify_id_token(access_token)
        uid = decoded_token['uid']
        # You can access additional user information from decoded_token
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Google access token")

        # Check if user exists in your database (optional)
        # If user doesn't exist, consider creating them based on UID

        # Generate and return a JWT or other authentication token
        # (Implementation details omitted for brevity)

    return {"message": "Successfully logged in with Google"}

@router.get("/logout", tags=['Authentication'])
async def logout():
    return {
        message: "Logout"
    }


@router.post("/signup", tags=['Authentication'])
async def signup(user: UserInput):
    try:
        auth.create_user(email=user.email, password=user.password)
        # auth.generate_email_verification_link(email=user.email)
        print(newHash)
        return JSONResponse(content={
            "message": "User registration successful"
        })


    
    except HTTPException:
        raise HTTPException(detail="Invalid credentials")

@router.get("/auth", tags=['Authentication'])
async def auth_callback():
    return