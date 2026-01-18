from common.db import users_collection
from datetime import datetime


def get_or_create_user(firebase_user):
    collection = users_collection()

    user = collection.find_one(
        {"firebase_uid": firebase_user["uid"]}
    )

    if user:
        return user

    new_user = {
        "firebase_uid": firebase_user["uid"],
        "email": firebase_user.get("email"),
        "created_at": datetime.utcnow(),
    }

    collection.insert_one(new_user)
    return new_user
