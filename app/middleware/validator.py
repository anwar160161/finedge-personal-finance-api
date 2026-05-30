from fastapi import HTTPException


def validate_transaction(transaction):

    if transaction.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Amount must be greater than zero"
        )

    if transaction.type.lower() not in [
        "income",
        "expense"
    ]:
        raise HTTPException(
            status_code=400,
            detail="Invalid transaction type"
        )