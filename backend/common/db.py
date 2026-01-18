from pymongo import MongoClient
import os

_client = None
_db = None


def get_db():
    global _client, _db

    if _db is None:
        mongo_uri = os.getenv("MONGO_URI")
        if not mongo_uri:
            raise Exception("MONGO_URI not set in environment")

        _client = MongoClient(mongo_uri)
        _db = _client["ai_travel_planner"]

    return _db


def users_collection():
    return get_db()["users"]


def trips_collection():
    return get_db()["trips"]
