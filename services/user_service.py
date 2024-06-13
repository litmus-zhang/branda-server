from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from models.schemas import UserInput
from firebase_admin import auth
from firebase_admin.auth import UserRecord
from firebase_admin.firestore import firestore

db = firestore.Client


class UserService:
    def get_user(self, user_id: str):
        pass

    def get_user_brands(self, user_id: str):
        pass

    def user_register(self, user: UserInput):
        try:
            get_user = auth.get_user_by_email(email=user.email)
            if get_user:
                raise HTTPException(
                    detail={"message": "User already exists"},
                    status_code=status.HTTP_409_CONFLICT,
                )
        except auth.UserNotFoundError:

            auth.create_user(email=user.email, password=user.password)
            return JSONResponse(
                content={"message": "User registration successful"},
                status_code=status.HTTP_201_CREATED,
            )

    def user_login(self, user: UserInput):
        try:
            user = auth.get_user_by_email(email=user.email)
            return JSONResponse(
                content={"message": "User login successful"},
                status_code=status.HTTP_200_OK,
            )
        except auth.UserNotFoundError:
            raise HTTPException(
                detail={"message": "User not found"},
                status_code=status.HTTP_404_NOT_FOUND,
            )
