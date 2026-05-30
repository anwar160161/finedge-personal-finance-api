import json
import uuid

USERS_FILE = "app/data/users.json"


async def get_all_users():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except:
        return []


async def create_user(user):
    users = await get_all_users()

    new_user = {
        "id": str(uuid.uuid4()),
        "name": user.name,
        "email": user.email,
        "password": user.password
    }

    users.append(new_user)

    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

    return {
        "message": "User created successfully",
        "user": new_user
    }