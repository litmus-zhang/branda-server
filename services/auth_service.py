from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from models.schemas import UserInput, UserRegister
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .auth_handler import decode_jwt


class AuthService:
    def __init__(self):
        pass

    def user_register(self, user: UserRegister):
        try:
            # Check if user already exists
            # if user exists, raise an exception
            # else create a new user hash the password and save the user
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
