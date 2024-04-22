import databases
from sqlalchemy import *
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
metadata = MetaData()

database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
