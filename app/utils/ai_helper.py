def generate_saving_tip(expense_amount):

    if expense_amount > 50000:
        return (
            "High spending detected. "
            "Consider reducing discretionary expenses."
        )

    if expense_amount > 20000:
        return (
            "Review your monthly subscriptions "
            "and dining expenses."
        )

    return (
        "Good spending habits. "
        "Continue tracking your finances."
    )