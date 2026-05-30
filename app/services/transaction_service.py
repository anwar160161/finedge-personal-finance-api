import json
import uuid

from app.utils.cache import clear_cache
from fastapi import HTTPException

TRANSACTIONS_FILE = "app/data/transactions.json"


async def get_transactions():
    try:
        with open(TRANSACTIONS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


async def create_transaction(transaction):
    transactions = await get_transactions()

    new_transaction = {
        "id": str(uuid.uuid4()),
        "type": transaction.type,
        "category": transaction.category,
        "amount": transaction.amount,
        "date": str(transaction.date)
    }

    transactions.append(new_transaction)

    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(transactions, file, indent=4)

    clear_cache()

    return {
        "message": "Transaction added successfully",
        "transaction": new_transaction
    }


async def get_transaction_by_id(transaction_id):
    transactions = await get_transactions()

    for transaction in transactions:
        if transaction["id"] == transaction_id:
            return transaction

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )


async def update_transaction(transaction_id, updated_transaction):
    transactions = await get_transactions()

    for transaction in transactions:
        if transaction["id"] == transaction_id:

            transaction["type"] = updated_transaction.type
            transaction["category"] = updated_transaction.category
            transaction["amount"] = updated_transaction.amount
            transaction["date"] = str(updated_transaction.date)

            with open(TRANSACTIONS_FILE, "w") as file:
                json.dump(transactions, file, indent=4)

            clear_cache()

            return {
                "message": "Transaction updated successfully",
                "transaction": transaction
            }

    raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )


async def delete_transaction(transaction_id):
    transactions = await get_transactions()

    transaction_exists = any(
        t["id"] == transaction_id
        for t in transactions
    )

    if not transaction_exists:
        raise HTTPException(
        status_code=404,
        detail="Transaction not found"
    )

    updated_transactions = [
        t for t in transactions
        if t["id"] != transaction_id
    ]

    with open(TRANSACTIONS_FILE, "w") as file:
        json.dump(updated_transactions, file, indent=4)

    clear_cache()

    return {
        "message": "Transaction deleted successfully"
    }