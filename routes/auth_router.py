from fastapi import APIRouter, Depends

from config.database import get_db
from services.auth_service import AuthService

auth_router = APIRouter(tags=["Authentication"])

auth_service = AuthService()
from models.schemas import UserInput, UserRegister
from sqlalchemy.orm import Session


@auth_router.post("/login")
async def login(user: UserInput, db: Session = Depends(get_db)):
    return auth_service.user_login(user, db)


@auth_router.post("/signup")
async def signup(user: UserRegister, db: Session = Depends(get_db)):
    return auth_service.user_register(user, db=db)
