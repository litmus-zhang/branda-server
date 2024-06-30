from fastapi import HTTPException
from fastapi.responses import JSONResponse
import passlib
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from models import models
from models.schemas import UserUpdate


class UserService:
    def update_user(self, user_id: str, data: UserUpdate, db: Session):
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if data.password:
            user.hashed_password = passlib.hash.bcrypt.hash(data.password)
        # Update user attributes directly
        if data.firstname:  # Assuming you want to update firstname as well
            user.firstname = data.firstname
        if data.lastname:
            user.lastname = data.lastname
        if data.email:
            user.email = data.email
        db.commit()
        return JSONResponse(
            content={
                "message": "User updated successfully",
            }
        )

    def get_user(self, user_id: str, db: Session):
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if not user:
            raise HTTPException(
                status_code=404, detail="User not found with the given id"
            )
        user_data = jsonable_encoder(user, exclude={"hashed_password"})
        return user_data

    def get_user_brands(self, user_id: str, db: Session):
        try:
            all_user_brands = (
                db.query(models.Brand).filter(models.Brand.owner_id == user_id).all()
            )
            return JSONResponse(
                content={
                    "message": "User brands received successfully",
                    "data": all_user_brands,
                }
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc
