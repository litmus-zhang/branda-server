from fastapi import APIRouter
from dotenv import load_dotenv
from routes.brand_router import brand_router
from routes.auth_router import auth_router
from routes.user_router import user_router

load_dotenv()


router = APIRouter()
router.include_router(auth_router)
router.include_router(user_router)
router.include_router(brand_router)


@router.get("/status", tags=["Health check"])
async def get_status():
    return {"message": "All system operational", "status": "OK"}
