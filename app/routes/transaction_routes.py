from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from app.schemas.transaction_schema import TransactionCreate
from app.dependencies import get_db

from app.controllers.transaction_controller import (
    add_transaction,
    fetch_transactions,
    fetch_transaction,
    edit_transaction,
    remove_transaction
)

from app.utils.analytics import (
    filter_by_category,
    filter_by_month
)

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post("")
async def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    return await add_transaction(
        transaction,
        db
    )


@router.get("")
async def get_transactions(
    db: Session = Depends(get_db)
):
    return await fetch_transactions(db)


@router.get("/analytics")
async def analytics(
    category: str | None = Query(None),
    month: int | None = Query(None),
    db: Session = Depends(get_db)
):
    transactions = await fetch_transactions(db)

    if category:
        return filter_by_category(
            transactions,
            category
        )

    if month:
        return filter_by_month(
            transactions,
            month
        )

    return transactions


@router.get("/{transaction_id}")
async def get_transaction(
    transaction_id: str,
    db: Session = Depends(get_db)
):
    return await fetch_transaction(
        transaction_id,
        db
    )


@router.patch("/{transaction_id}")
async def update_transaction(
    transaction_id: str,
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):
    return await edit_transaction(
        transaction_id,
        transaction,
        db
    )


@router.delete("/{transaction_id}")
async def delete_transaction(
    transaction_id: str,
    db: Session = Depends(get_db)
):
    return await remove_transaction(
        transaction_id,
        db
    )