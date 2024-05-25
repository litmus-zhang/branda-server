from fastapi import APIRouter, Query, Depends
from restcountries import RestCountryApiV2 as rapi
import os
import requests
from typing import Annotated
from dotenv import load_dotenv
from config import langchain_helper as lch
from models.schemas import Strategy, Base
import random
from config.config import get_firebase_user_from_token
from config.helper import brands


load_dotenv()

router = APIRouter()


@router.get("/status")
async def get_status():
    return {
        "message": "All system operation",
        "status": "OK"
    }

@router.get("/font")
async def create_font():
    API_KEY = os.getenv("GOOGLE_FONTS_API_KEY")
    url = "https://www.googleapis.com/webfonts/v1/webfonts?key=" + API_KEY
    response =  requests.get(url, timeout=5)

    fonts = response.json()
    list_of_fonts = fonts['items']

    # Select 3 random fonts
    random_fonts = random.sample(list_of_fonts, 3)

    return {"fonts": random_fonts}


@router.get("/color")
async def create_color_pallete(base: Base):
    response = lch.generate_brand_color(niche=base.niche, industry=base.industry)
    return {"response" : response}


@router.get("/messaging")
def create_brand_messaging(base: Base):
    response = lch.generate_brand_messaging(industry=base.industry, niche=base.niche)
    return {"response" : response}

@router.get("/strategy")
def create_brand_strategy(brand_strategy: Strategy):
    industry = brand_strategy.industry
    niche = brand_strategy.niche
    country = brand_strategy.country
    response = lch.generate_business_strategy(industry=industry, niche=niche, country=country)
    return {"response" : response}

@router.get("/brand_name")
def generate_brand_name(base: Base):
    response = lch.generate_brand_name(niche=base.niche, industry=base.industry)
    return {"response" : response}


@router.get("/logo")
def create_logo(base: Base):
    response = lch.generate_logo(industry=base.industry, niche=base.niche)
    return {"response" : response}

@router.get("/photography")
def create_photography(base: Base):
    response = lch.generate_pics(industry=base.industry)
    return {"response" : response}


@router.get("/illustration")
def create_illustration(base: Base):
    response = lch.generate_pattern(industry=base.industry)
    return {"response" : response}


@router.get("/all-countries/")
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