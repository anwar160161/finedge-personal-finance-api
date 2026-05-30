from fastapi import FastAPI

from app.routes.user_routes import router as user_router
from app.routes.transaction_routes import router as transaction_router
from app.routes.summary_routes import router as summary_router

from app.middleware.logger import LoggerMiddleware
from app.middleware.error_handler import global_exception_handler
from app.routes.auth_routes import router as auth_router

app = FastAPI(title="FinEdge API")

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