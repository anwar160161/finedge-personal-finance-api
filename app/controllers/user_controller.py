from app.services.user_service import create_user, get_all_users

async def register_user(user):
    return await create_user(user)

async def fetch_users():
    return await get_all_users()