from fastapi import APIRouter
from app.controllers.summary_controller import (
    fetch_summary
)

router = APIRouter(
    tags=["Summary"]
)

@router.get("/summary")
async def get_summary():
    return await fetch_summary()