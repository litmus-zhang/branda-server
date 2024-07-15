from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
import passlib.hash
from models.schemas import UserInput, UserRegister
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from models import models
import passlib

from .auth_handler import decode_jwt, sign_jwt


class AuthService:

    def user_register(self, user: UserRegister, db: Session):
        try:
            # Check if user already exists
            if (
                db.query(models.User).filter(models.User.email == user.email).first()
                is not None
            ):
                raise HTTPException(
                    detail="User already registered",
                    status_code=status.HTTP_400_BAD_REQUEST,
                )
            # Else, create a new user, hash the password, and save the user
            hashed_password = passlib.hash.bcrypt.hash(user.password)
            new_user = models.User(
                **user.model_dump(exclude={"password"}), hashed_password=hashed_password
            )
            db.add(new_user)
            db.commit()  # Commit the transaction to save the user to the database
            db.refresh(
                new_user
            )  # Refresh the instance with the new data from the database
            return {"message": "User created successfully"}
        except Exception as e:
            db.rollback()
            raise HTTPException(
                detail=str(e),
                status_code=status.HTTP_403_FORBIDDEN,
            ) from e

    def user_login(self, user: UserInput, db: Session):
        try:
            # Check if user exists
            findUser = (
                db.query(models.User).filter(models.User.email == user.email).first()
            )
            if findUser is None:
                raise HTTPException(
                    detail={"message": "User not found"},
                    status_code=status.HTTP_404_NOT_FOUND,
                )
            # else check if password matches
            if not passlib.hash.bcrypt.verify(user.password, findUser.hashed_password):
                raise HTTPException(
                    detail={"message": "Invalid credentials"},
                    status_code=status.HTTP_401_UNAUTHORIZED,
                )
            # if user exists, return a token nd a message
            token = sign_jwt(findUser.id)

            # else raise an exception
            return JSONResponse(
                content={"message": "User login successful", "token": token},
                status_code=status.HTTP_200_OK,
            )
        except Exception as e:
            raise HTTPException(
                detail=str(e),
                status_code=status.HTTP_403_FORBIDDEN,
            ) from e


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True

        return isTokenValid
