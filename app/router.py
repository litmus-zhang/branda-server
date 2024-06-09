from fastapi import APIRouter, Query, Depends, Body
from restcountries import RestCountryApiV2 as rapi
import os
import requests
from typing import Annotated
from dotenv import load_dotenv
from config import langchain_helper as lch
from models.schemas import Strategy, Base, BaseBody
import random
from config.config import get_firebase_user_from_token
from config.helper import brands


load_dotenv()

router = APIRouter()


@router.get("/status", tags=["Health check"])
async def get_status():
    return {
        "message": "All system operational",
        "status": "OK"
    }
@router.get("/font", tags=["Brand"])
async def get_font():
    API_KEY = os.getenv("GOOGLE_FONTS_API_KEY")
    url = "https://www.googleapis.com/webfonts/v1/webfonts?key=" + API_KEY
    response =  requests.get(url, timeout=5)

    fonts = response.json()
    list_of_fonts = fonts['items']

    # Select 3 random fonts
    random_fonts = random.sample(list_of_fonts, 3)

    return {"fonts": random_fonts}

@router.get("/font", tags=["Brand"])
async def create_font():
    API_KEY = os.getenv("GOOGLE_FONTS_API_KEY")
    url = "https://www.googleapis.com/webfonts/v1/webfonts?key=" + API_KEY
    response =  requests.get(url, timeout=5)

    fonts = response.json()
    list_of_fonts = fonts['items']

    # Select 3 random fonts
    random_fonts = random.sample(list_of_fonts, 3)

    return {"fonts": random_fonts}


@router.get("/color", tags=["Brand"])
async def get_color_pallete(base: Base):
    response = lch.generate_brand_color(niche=base.niche, industry=base.industry)
    return {"response" : response}

@router.post("/color", tags=["Brand"])
async def create_color_pallete(base: Base):
    response = lch.generate_brand_color(niche=base.niche, industry=base.industry)
    return {"response" : response}


@router.get("/messaging", tags=["Brand"])
def get_brand_messaging(base: Base):
    response = lch.generate_brand_messaging(industry=base.industry, niche=base.niche)
    return {"response" : response}

@router.post("/messaging", tags=["Brand"])
def create_brand_messaging(base: Base):
    response = lch.generate_brand_messaging(industry=base.industry, niche=base.niche)
    return {"response" : response}

@router.get("/strategy", tags=["Brand"])
def get_brand_strategy(brand_strategy: Strategy):
    industry = brand_strategy.industry
    niche = brand_strategy.niche
    country = brand_strategy.country
    response = lch.generate_business_strategy(industry=industry, niche=niche, country=country)
    return {"response" : response}

@router.post("/strategy", tags=["Brand"])
def create_brand_strategy(brand_strategy: Strategy):
    industry = brand_strategy.industry
    niche = brand_strategy.niche
    country = brand_strategy.country
    response = lch.generate_business_strategy(industry=industry, niche=niche, country=country)
    return {"response" : response}

@router.get("/brand_name", tags=["Brand"])
def get_brand_name(base: Base):
    response = lch.generate_brand_name(niche=base.niche, industry=base.industry)
    return {"data" : response, "message": "Brand names fetched successfully"}

@router.post("/brand_name", tags=["Brand"], status_code=201)
def post_brand_name(base: BaseBody):
    print(base.name)
    # Store brand name in firebase
    return {"message" : "Brand name saved successfully"}


@router.get("/logo", tags=["Brand"])
def get_logo(base: Base):
    response = lch.generate_logo(industry=base.industry, niche=base.niche)
    return {"response" : response}

@router.post("/logo", tags=["Brand"])
def create_logo(base: Base):
    response = lch.generate_logo(industry=base.industry, niche=base.niche)
    return {"response" : response}

@router.get("/photography", tags=["Brand"])
def get_photography(base: Base):
    response = lch.generate_pics(industry=base.indus)
    return {"response" : response}

@router.post("/photography", tags=["Brand"])
def create_photography(base: Base):
    response = lch.generate_pics(industry=base.industry)
    return {"response" : response}

@router.get("/illustration", tags=["Brand"])
def get_illustration(base: Base):
    response = lch.generate_pattern(industry=base.industry)
    return {"response" : response}

@router.post("/illustration", tags=["Brand"])
def create_illustration(base: Base):
    response = lch.generate_pattern(industry=base.industry)
    return {"response" : response}

@router.get("/all-brand/:id", tags=["Brand"])
def get_all_user_brand():
    return {
        "message": "All user brand",
        "data": []
    }


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


@router.get("/userId")
async def get_userid(user: Annotated[dict, Depends(get_firebase_user_from_token)]):
    return {"id": user["uid"]}

@router.get("/login", tags=['Authentication'])
async def login():
    return {
        message: "Login with Google"
    }

@router.get("/logout", tags=['Authentication'])
async def logout():
    return {
        message: "Login with Google"
    }
@router.get("/auth", tags=['Authentication'])
async def auth_callback():
    return