from jose import jwt
import os
from dotenv import load_dotenv

load_dotenv()


def decode_token(token: str):
    try:
        return jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
    except:
        return None
