import os
import pathlib
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin.auth import verify_id_token

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


def get_firebase_user_from_token( token: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],) -> dict | None:
    try:
        if not token:
            raise ValueError("No Token")
        user = verify_id_token(token.credentials)
        return user
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not logged in or invalid credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
