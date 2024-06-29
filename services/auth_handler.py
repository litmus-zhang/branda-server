import time
from typing import Dict

import jwt
from decouple import config


JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")


def token_response(token: str):
    return {"access_token": token}


def sign_jwt(user_id: int | str) -> Dict[str, str]:
    payload = {"user_id": user_id, "expires": time.time() + 60 * 30}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decode_jwt(token: str) -> Dict[str, str]:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token is expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}