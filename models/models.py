from pydantic import BaseModel
from config.config import Base
from datetime import date, time
from sqlalchemy import MetaData, Column, Integer, String, ForeignKey,Table
from sqlalchemy.orm import relationship
from config.config import metadata



business_details = Table(
    "business_details",
    metadata,
    Column('id', ForeignKey("users.id") ,primary_key=True),
    Column('nich', String),
    Column('description', String),
    Column('target_audience', String),
    Column('country', String),
    relationship('user',"User", back_populates="business_details")
)

users = Table(
   "users",
   metadata,
    Column('id',Integer, primary_key=True),
    Column('first_name',String),
    Column('last_name',String),
    Column('email',String),
    Column('social_id',String),
    relationship('brands',"Brands", back_populates="user",),
    relationship('business_details',"BusinessDetails", back_populates="user")
)

brands= Table(
    "brands",
    Column('id',Integer, ForeignKey("users.id"), primary_key=True ),
    Column('name',String),
    Column('logo',String),
    Column('color',String),
    Column('font',String),
    Column('messaging',String),
    Column('photography',String),
    Column('Illustration',String),
    relationship('user',"User", back_populates="brands")
)
