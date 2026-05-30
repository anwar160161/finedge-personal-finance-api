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
async def add_transaction(transaction):
    return await create_transaction(transaction)

async def fetch_transactions():
    return await get_transactions()

async def fetch_transaction(transaction_id):
    return await get_transaction_by_id(transaction_id)

async def edit_transaction(transaction_id, transaction):
    return await update_transaction(transaction_id, transaction)

async def remove_transaction(transaction_id):
    return await delete_transaction(transaction_id)

async def add_transaction(transaction):

    validate_transaction(transaction)

    return await create_transaction(
        transaction
    )