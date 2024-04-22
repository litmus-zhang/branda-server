import databases
from sqlalchemy import *
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
metadata = MetaData()

database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
