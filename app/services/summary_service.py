from app.services.transaction_service import get_transactions
from app.utils.cache import get_cache, set_cache
from app.utils.ai_helper import generate_saving_tip


async def get_summary(db):

    cached_summary = get_cache("summary")

    if cached_summary:
        return cached_summary

    transactions = await get_transactions(db)

    income = sum(
        t.amount
        for t in transactions
        if t.type.lower() == "income"
    )

    expense = sum(
        t.amount
        for t in transactions
        if t.type.lower() == "expense"
    )

    summary = {
        "income": income,
        "expense": expense,
        "balance": income - expense,
        "saving_tip": generate_saving_tip(expense)
    }

    set_cache(
        "summary",
        summary,
        ttl=60
    )

    return summary