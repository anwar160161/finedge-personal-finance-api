from pydantic import BaseModel
from datetime import date

class Transaction(BaseModel):
    type: str
    category: str
    amount: float
    date: date