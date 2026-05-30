from datetime import datetime


def filter_by_category(transactions, category):
    return [
        transaction
        for transaction in transactions
        if transaction.category.lower()
        == category.lower()
    ]


def filter_by_month(transactions, month):
    filtered = []

    for transaction in transactions:

        transaction_month = datetime.strptime(
            transaction.date,
            "%Y-%m-%d"
        ).month

        if transaction_month == month:
            filtered.append(transaction)

    return filtered


def monthly_trend(transactions):

    trends = {}

    for transaction in transactions:

        month = transaction.date[:7]

        trends.setdefault(
            month,
            {
                "income": 0,
                "expense": 0
            }
        )

        if transaction.type.lower() == "income":
            trends[month]["income"] += transaction.amount
        else:
            trends[month]["expense"] += transaction.amount

    return trends