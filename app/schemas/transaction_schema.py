from pydantic import BaseModel
from datetime import date


class TransactionCreate(BaseModel):
    type: str
    category: str
    amount: float
    date: date


class TransactionResponse(BaseModel):
    id: str
    type: str
    category: str
    amount: float
    date: str

    class Config:
        from_attributes = True