from fastapi import FastAPI

from app.routes.user_routes import router as user_router
from app.routes.transaction_routes import router as transaction_router
from app.routes.summary_routes import router as summary_router

from app.middleware.logger import LoggerMiddleware
from app.middleware.error_handler import global_exception_handler
from app.routes.auth_routes import router as auth_router
from app.database import Base, engine

app = FastAPI(
    title="FinEdge Personal Finance API",
    description="""
    Personal Finance Management API built with FastAPI, SQLAlchemy, and SQLite.

    Features:
    • User Management
    • JWT Authentication
    • Transaction Tracking
    • Financial Summary
    • Analytics & Reporting
    • AI Saving Tips
    """,
    version="2.0.0",
    contact={
        "name": "Anwar Shaik",
        "email": "anwar160161@gmail.com"
    }

)

Base.metadata.create_all(bind=engine)

app.add_middleware(LoggerMiddleware)
app.include_router(auth_router)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

@app.get("/health")
async def health():
    return {"status": "running"}

app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(summary_router)