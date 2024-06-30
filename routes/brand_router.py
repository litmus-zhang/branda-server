from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from config.database import get_db
from models.schemas import BaseBody, Base, Strategy, User
from routes.user_router import get_current_user
from services.brand_service import BrandService
from services.auth_service import JWTBearer
from sqlalchemy.orm import Session


brand_service = BrandService()

brand_router = APIRouter(tags=["Brand"], dependencies=[Depends(JWTBearer())])


@brand_router.get("/font")
async def get_font():
    try:
        data = brand_service.get_font()
        return JSONResponse(
            content={"message": "Font Received Successfully", "data": data}
        )
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@brand_router.post("/users/brands/{brandId}/font")
async def create_font(base: BaseBody, brandId: str, db: Session = Depends(get_db)):
    return brand_service.store_font(base, brandId, db=db)


@brand_router.get("/color")
async def get_color_pallete(base: Base):
    try:
        data = brand_service.get_color_pallete(base)
        return JSONResponse(
            content={"message": "Color pallete received successfully", "data": data}
        )
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Error getting data") from exc


@brand_router.post("/users/brands/{brandId}/color")
async def create_color_pallete(
    base: BaseBody, brandId: str, db: Session = Depends(get_db)
):
    return brand_service.store_color_pallete(base, brandId, db=db)


@brand_router.get("/messaging")
def get_brand_messaging(base: Base):
    try:

        data = brand_service.get_brand_messaging(base)
        return JSONResponse(
            content={"message": "Brand messaging received Successfully", "data": data}
        )
    except Exception as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@brand_router.post("/users/brands/{brandId}/messaging")
def create_brand_messaging(base: BaseBody, brandId: str, db: Session = Depends(get_db)):
    return brand_service.store_brand_messaging(base, brandId, db=db)


@brand_router.get("/strategy")
def get_brand_strategy(brand_strategy: Strategy):
    try:
        data = brand_service.get_brand_strategy(brand_strategy)
        return JSONResponse(
            content={"message": "Brand strategy received successfully", "data": data}
        )
    except Exception as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@brand_router.post("/users/brands/{brandId}/strategy")
def create_brand_strategy(
    brand_strategy: BaseBody, brandId: str, db: Session = Depends(get_db)
):
    return brand_service.store_brand_strategy(brand_strategy, brandId, db=db)


@brand_router.get("/brand_name")
def get_brand_name(base: Base):
    try:
        data = brand_service.get_brand_name(base)
        return JSONResponse(
            content={"message": "Brand names fetched successfully", "data": data}
        )
    except Exception as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@brand_router.post("/users/brands/brand_name", status_code=201)
def post_brand_name(
    base: BaseBody,
    user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    print(user, base)
    return brand_service.store_brand_name(base, userId=user["id"], db=db)


@brand_router.get("/logo")
def get_logo(base: Base):
    try:
        return brand_service.get_logo(base)

    except Exception as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@brand_router.post("/users/brands/{brandId}/logo")
def create_logo(base: BaseBody, brandId: str, db: Session = Depends(get_db)):
    return brand_service.store_brand_logo(base, brandId, db=db)


@brand_router.get("/photography")
def get_photography(base: Base):
    try:
        return brand_service.get_photography(base)
    except Exception as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@brand_router.post("/users/brands/{brandId}/photography")
def create_photography(base: BaseBody, brandId: str, db: Session = Depends(get_db)):
    return brand_service.store_brand_photography(base, brandId, db=db)


@brand_router.get("/illustration")
def get_illustration(base: Base):
    try:
        return brand_service.get_illustration(base)
    except Exception as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@brand_router.post("/users/brands/{brandId}/illustration")
def create_illustration(base: BaseBody, brandId: str, db: Session = Depends(get_db)):
    return brand_service.store_brand_illustration(base, brandId, db=db)


@brand_router.put("/users/brands/{brandId}")
def update_brand_details(
    base: BaseBody, userId: str, brandId: str, db: Session = Depends(get_db)
):
    return brand_service.update_brand_details(base, brandId, userId, db=db)
