import os
import pathlib
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

bearer_scheme=HTTPBearer(auto_error=False)

basedir = pathlib.Path(__file__).parents[1]
load_dotenv(basedir/".env")

class Settings(BaseSettings):
    "Main settings"
    app_name: str = "branda-firebase"
    env: str = os.getenv("ENV", "developement")
    frontend_url: str = os.getenv("FRONTEND_URL", "NA")

@lru_cache
def get_settings() -> Settings:
    "Retrieves app setting"
    return Settings


