from app.services.transaction_service import (
    create_transaction,
    get_transactions,
    get_transaction_by_id,
    update_transaction,
    delete_transaction
)

from app.middleware.validator import (
    validate_transaction
)


async def add_transaction(
    transaction,
    db
):
    validate_transaction(transaction)

    return await create_transaction(
        transaction,
        db
    )


async def fetch_transactions(db):
    return await get_transactions(db)


async def fetch_transaction(
    transaction_id,
    db
):
    return await get_transaction_by_id(
        transaction_id,
        db
    )


async def edit_transaction(
    transaction_id,
    transaction,
    db
):
    return await update_transaction(
        transaction_id,
        transaction,
        db
    )


async def remove_transaction(
    transaction_id,
    db
):
    return await delete_transaction(
        transaction_id,
        db
    )