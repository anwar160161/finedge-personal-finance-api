import uuid

from fastapi import HTTPException

from app.models.transaction import Transaction
from app.utils.cache import clear_cache


async def get_transactions(db):
    return db.query(Transaction).all()


async def create_transaction(transaction_data, db):

    transaction = Transaction(
        id=str(uuid.uuid4()),
        type=transaction_data.type,
        category=transaction_data.category,
        amount=transaction_data.amount,
        date=str(transaction_data.date)
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    clear_cache()

    return {
        "message": "Transaction added successfully",
        "transaction": {
            "id": transaction.id,
            "type": transaction.type,
            "category": transaction.category,
            "amount": transaction.amount,
            "date": transaction.date
        }
    }


async def get_transaction_by_id(transaction_id, db):

    transaction = (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id)
        .first()
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction


async def update_transaction(
    transaction_id,
    updated_transaction,
    db
):

    transaction = (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id)
        .first()
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    transaction.type = updated_transaction.type
    transaction.category = updated_transaction.category
    transaction.amount = updated_transaction.amount
    transaction.date = str(updated_transaction.date)

    db.commit()

    clear_cache()

    return {
        "message": "Transaction updated successfully"
    }


async def delete_transaction(
    transaction_id,
    db
):

    transaction = (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id)
        .first()
    )

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    db.delete(transaction)
    db.commit()

    clear_cache()

    return {
        "message": "Transaction deleted successfully"
    }