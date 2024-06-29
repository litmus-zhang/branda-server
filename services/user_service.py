from fastapi import HTTPException
from fastapi.responses import JSONResponse
import passlib
from sqlalchemy.orm import Session

from models import models
from models.schemas import UserRegister


class UserService:
    def update_user(self, user_id: str, data: UserRegister, db: Session):
        # Check if user exists
        # if user exists, update user data
        # else raise an exception
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user:
            hashed_password = passlib.hash.bcrypt.hash(data.password)
            updated_user = user.update(
                **data.model_dump(exclude={"password"}), hashed_password=hashed_password
            )
            db.commit()
            return JSONResponse(
                content={
                    "message": "User updated successfully",
                }
            )
        else:
            raise HTTPException(
                status_code=404, detail="User not found with the given id"
            )

    def get_user(self, user_id: str, db: Session):
        # Check if user exists
        # if user exists, return user data
        # else raise an exception
        user = db.query(models.User).filter(models.User.id == user_id).first()
        return JSONResponse(
            content={"message": "User received successfully", "data": user.to_dict()}
        )

    def get_user_brands(self, user_id: str, db: Session):
        try:
            all_user_brands = (
                db.query(models.Brand).filter(models.Brand.user_id == user_id).all()
            )
            return JSONResponse(
                content={
                    "message": "User brands received successfully",
                    "data": all_user_brands,
                }
            )
        except Exception as exc:
            raise HTTPException(detail={"message": str(exc)}, status_code=404) from exc
