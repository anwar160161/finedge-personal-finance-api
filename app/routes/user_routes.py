from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.controllers.user_controller import (
    register_user,
    fetch_users,
    fetch_user,
    remove_user
)
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("")
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return await register_user(
        user,
        db
    )

@router.get("")
async def get_users(
    db: Session = Depends(get_db)
):
    return await fetch_users(db)

@router.get("/{user_id}")
async def get_user(
    user_id: str,
    db: Session = Depends(get_db)
):
    return await fetch_user(
        user_id,
        db
    )

@router.delete("/{user_id}")
async def delete_user(
    user_id: str,
    db: Session = Depends(get_db)
):
    return await remove_user(
        user_id,
        db
    )