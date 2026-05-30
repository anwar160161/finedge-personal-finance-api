from fastapi import APIRouter
from app.models.user import User
from app.controllers.user_controller import (
    register_user,
    fetch_users
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("")
async def create_user(user: User):
    return await register_user(user)

@router.get("")
async def get_users():
    return await fetch_users()