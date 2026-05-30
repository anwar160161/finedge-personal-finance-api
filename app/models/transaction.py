from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Float

from app.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True)
    type = Column(String)
    category = Column(String)
    amount = Column(Float)
    date = Column(String)