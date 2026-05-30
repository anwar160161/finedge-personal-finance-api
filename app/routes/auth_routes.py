from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

SECRET_KEY = os.getenv("SECRET_KEY")

class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
async def login(data: LoginRequest):

    token = jwt.encode(
        {
            "email": data.email
        },
        SECRET_KEY,
        algorithm="HS256"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }