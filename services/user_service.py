from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from models.schemas import UserInput


class UserService:
    def __init__(self):
        self.db = ""

    def get_user(self, user_id: str):
        # Check if user exists
        # if user exists, return user data
        # else raise an exception
        return JSONResponse(
            content={"message": "User received successfully", "data": "user"}
        )

    def get_user_brands(self, user_id: str):
        try:
            all_user_brands = "Hello from user_service.py get_user_brands method"
            user_brands = [brand.to_dict() for brand in all_user_brands]
            return JSONResponse(
                content={
                    "message": "User brands received successfully",
                    "data": user_brands,
                }
            )
        except Exception as exc:
            raise HTTPException(
                detail={"message": "Error getting data"}, status_code=404
            ) from exc

   