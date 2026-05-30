from app.services.summary_service import get_summary

async def fetch_summary():
    return await get_summary()