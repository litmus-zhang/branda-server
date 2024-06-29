from fastapi import APIRouter

from services.auth_service import AuthService

auth_router = APIRouter(tags=["Authentication"])

auth_service = AuthService()
from models.schemas import UserInput, UserRegister


@auth_router.post("/login")
async def login(user: UserInput):
    return auth_service.user_login(user)


@auth_router.post("/signup")
async def signup(user: UserRegister):
    return auth_service.user_register(user)
