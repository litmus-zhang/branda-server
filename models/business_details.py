from pydantic import BaseModel
from config.config import db




class BusinessDetails(BaseModel):
    niche: str
    description: str
    target_audience: str
    country: str