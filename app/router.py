from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException
from dotenv import load_dotenv
from services.brand_service import BrandService
from services.user_service import UserService
from models.schemas import Strategy, Base, BaseBody, UserInput

load_dotenv()

bearer_scheme = HTTPBearer(auto_error=False)
brand_service = BrandService()
user_Service = UserService()

router = APIRouter()


def get_current_user(
    token: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)]
) -> dict | None:
    try:
        # if not token:
        #     raise HTTPException(status_code=401, detail="No token provided")
        # user = auth.verify_id_token(token.credentials)
        # print(user)
        user = "1234"
        return user

    except Exception as exc:
        raise HTTPException(status_code=401, detail="Invalid credentials") from exc


@router.get("/users/me", tags=["User"])
async def get_user_id(user: Annotated[dict, Depends(get_current_user)]):
    return {"userId": user}


@router.get("/status", tags=["Health check"])
async def get_status():
    return {"message": "All system operational", "status": "OK"}


@router.get("/font", tags=["Brand"])
async def get_font():
    try:
        data = brand_service.get_font()
        return JSONResponse(
            content={"message": "Font Received Successfully", "data": data}
        )
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@router.post("/users/{userId}/brands/{brandId}/font", tags=["Brand"])
async def create_font(base: BaseBody, userId: str, brandId: str):
    return brand_service.store_font(base, userId, brandId)


@router.get("/color", tags=["Brand"])
async def get_color_pallete(base: Base):
    try:
        data = brand_service.get_color_pallete(base)
        return JSONResponse(
            content={"message": "Color pallete received successfully", "data": data}
        )
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@router.post("/users/{userId}/brands/{brandId}/color", tags=["Brand"])
async def create_color_pallete(base: BaseBody, userId: str, brandId: str):
    return brand_service.store_color_pallete(base, brandId, userId)


@router.get("/messaging", tags=["Brand"])
def get_brand_messaging(base: Base):
    try:

        data = brand_service.get_brand_messaging(base)
        return JSONResponse(
            content={"message": "Brand messaging received Successfully", "data": data}
        )
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@router.post("/users/{userId}/brands/{brandId}/messaging", tags=["Brand"])
def create_brand_messaging(base: BaseBody, userId: str, brandId: str):
    return brand_service.store_brand_messaging(base, brandId, userId)


@router.get("/strategy", tags=["Brand"])
def get_brand_strategy(brand_strategy: Strategy):
    try:
        data = brand_service.get_brand_strategy(brand_strategy)
        return JSONResponse(
            content={"message": "Brand strategy received successfully", "data": data}
        )
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@router.post("/users/{userId}/brands/{brandId}/strategy", tags=["Brand"])
def create_brand_strategy(brand_strategy: BaseBody, userId: str, brandId: str):
    return brand_service.store_brand_strategy(brand_strategy, brandId, userId)


@router.get("/brand_name", tags=["Brand"])
def get_brand_name(base: Base):
    try:
        data = brand_service.get_brand_name(base)
        return JSONResponse(
            content={"message": "Brand names fetched successfully", "data": data}
        )
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@router.post("/users/{userId}/brands/brand_name", tags=["Brand"], status_code=201)
def post_brand_name(base: BaseBody, userId: str):
    return brand_service.store_brand_name(base, userId)


@router.get("/logo", tags=["Brand"])
def get_logo(base: Base):
    try:
        return brand_service.get_logo(base)

    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@router.post("/users/{userId}/brands/{brandId}/logo", tags=["Brand"])
def create_logo(base: BaseBody, userId: str, brandId: str):
    return brand_service.store_brand_logo(base, brandId, userId)


@router.get("/photography", tags=["Brand"])
def get_photography(base: Base):
    try:
        return brand_service.get_photography(base)
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@router.post("/users/{userId}/brands/{brandId}/photography", tags=["Brand"])
def create_photography(base: BaseBody, userId: str, brandId: str):
    return brand_service.store_brand_photography(base, brandId, userId)


@router.get("/illustration", tags=["Brand"])
def get_illustration(base: Base):
    try:
        return brand_service.get_illustration(base)
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@router.post("/users/{userId}/brands/{brandId}/illustration", tags=["Brand"])
def create_illustration(base: BaseBody, userId: str, brandId: str):
    return brand_service.store_brand_illustration(base, brandId, userId)


@router.put("/users/{userId}/brands/{brandId}", tags=["Brand"])
def update_brand_details(base: BaseBody, userId: str, brandId: str):
    return brand_service.update_brand_details(base, brandId, userId)


@router.get("/users/{userId}/brands", tags=["User"])
def get_all_user_brand(userId: str):
    return user_Service.get_user_brands(userId)


@router.get("/users/me", tags=["User"])
def get_user_details(userId: str):
    data = "User data fetched successfully"
    return JSONResponse(content={"message": "Fetched users data", "data": data})


@router.post("/login", tags=["Authentication"])
async def login(user: UserInput):
    return user_Service.user_login(user)


@router.post("/signup", tags=["Authentication"])
async def signup(user: UserInput):
    return user_Service.user_register(user)
