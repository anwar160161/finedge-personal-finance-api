from fastapi import APIRouter, Query

from app.models.transaction import Transaction

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
    transaction: Transaction
):
    return await add_transaction(transaction)


@router.get("")
async def get_transactions():
    return await fetch_transactions()


# IMPORTANT:
# Place analytics BEFORE /{transaction_id}
@router.get("/analytics")
async def analytics(
    category: str | None = Query(None),
    month: int | None = Query(None)
):
    transactions = await fetch_transactions()

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
    transaction_id: str
):
    return await fetch_transaction(
        transaction_id
    )


@router.patch("/{transaction_id}")
async def update_transaction(
    transaction_id: str,
    transaction: Transaction
):
    return await edit_transaction(
        transaction_id,
        transaction
    )


@router.delete("/{transaction_id}")
async def delete_transaction(
    transaction_id: str
):
    return await remove_transaction(
        transaction_id
    )