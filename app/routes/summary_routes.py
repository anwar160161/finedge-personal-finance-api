from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.summary_controller import (
    fetch_summary
)

from app.dependencies import get_db

router = APIRouter(
    tags=["Summary"]
)


@router.get("/summary")
async def get_summary(
    db: Session = Depends(get_db)
):
    return await fetch_summary(db)