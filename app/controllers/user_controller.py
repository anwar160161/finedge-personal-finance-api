from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    delete_user
)

async def register_user(user, db):
    return await create_user(user, db)

async def fetch_users(db):
    return await get_all_users(db)

async def fetch_user(user_id, db):
    return await get_user_by_id(
        user_id,
        db
    )

async def remove_user(user_id, db):
    return await delete_user(
        user_id,
        db
    )