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

    def user_register(self, user: UserInput):
        try:
            # Check if user already exists
            # if user exists, raise an exception
            # else create a new user
            return JSONResponse(
                content={"message": "User registered successfully"},
                status_code=status.HTTP_201_CREATED,
            )
        except Exception:
            raise HTTPException(
                detail={"message": "Error registering user"}, status_code=404
            ) from None

    def user_login(self, user: UserInput):
        try:
            # Check if user exists
            # if user exists, return a token nd a message
            # else raise an exception
            return JSONResponse(
                content={"message": "User login successful", "token": "token"},
                status_code=status.HTTP_200_OK,
            )
        except Exception:
            raise HTTPException(
                detail={"message": "User not found"},
                status_code=status.HTTP_404_NOT_FOUND,
            ) from None
