from fastapi import Body, FastAPI, HTTPException, Depends, Query
import requests
from restcountries import RestCountryApiV2 as rapi
import os
from typing import Annotated, Optional, Union
from dotenv import load_dotenv
import config.langchain_helper as lch
from contextlib import asynccontextmanager
from config.config import engine, metadata, database
from fastapi.security import OAuth2PasswordBearer

from models.schemas import BusinessDetails

load_dotenv()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the database models and create tables
    metadata.create_all(engine)
    await database.connect()
    yield
    # Clean up the database and release the resources
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

# add orm and database setup [DONE]
# add google login

# add api versioning

# deploy the application to live

@app.get('/items')
async def get_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@app.post("/business-details")
async def create_business_details(business_details: BusinessDetails):
    business_details.country = business_details.country
    business_details_dict = {
        "niche": business_details.niche,
        "description": business_details.description,
        "target_audience": business_details.target_audience,
        "country": business_details.country
    }
    return business_details_dict

@app.get("/font")
async def create_font():
    API_KEY = os.getenv("GOOGLE_FONTS_API_KEY")
    url = "https://www.googleapis.com/webfonts/v1/webfonts?key=" + API_KEY
    response =  requests.get(url)
    fonts = response.json()
    return fonts['items']


@app.post("/color")
async def create_color_pallete(data: dict = Body(...)):
    url = "http://colormind.io/api/"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise exception for non-200 status codes

        palette = response.json()["result"]
        return palette

    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching palette: {e}")


@app.get("/messaging")
def create_brand_messaging():
    response = lch.generate_brand_messaging("Finance", "Targeting middle class citizens")
    return {"response" : response}

@app.get("/brand_name")
def generate_brand_name():
    response = lch.generate_brand_name("Finance", "Targeting middle class citizens")
    return {"response" : response}


@app.get("/logo")
def create_logo():
    response = lch.generate_logo("Finance", "Targeting middle class citizens")
    return {"response" : response}

@app.get("/photography")
def create_photography():
    response = lch.generate_pics("Finance")
    return {"response" : response}


@app.get("/illustration")
def create_illustration():
    response = lch.generate_pattern("Finance")
    return {"response" : response}


@app.get("/all-countries/")
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