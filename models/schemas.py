from pydantic import BaseModel

class Strategy(BaseModel):
    industry: str
    niche: str
    country: str

class Base(BaseModel):
    niche : str
    industry : str


class BaseBody(BaseModel):
    name: str | None = None
    font: str | None = None
    strategy: str | None = None
    color: str | None = None
    logo: str | None = None
    messaging: str | None = None
    photography: str | None = None
    illustration: str | None = None
    presentation: str | None = None

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

