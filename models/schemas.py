from pydantic import BaseModel

class BusinessDetails(BaseModel):
    niche: str
    description: str
    target_audience: str
    country: str

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    social_id: str

class Brands(BaseModel):
    name: str
    logo: str
    color: str
    font: str
    messaging: str
    photography: str
    Illustration: str
    business_details: BusinessDetails

