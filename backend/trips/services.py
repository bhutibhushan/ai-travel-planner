from common.db import trips_collection
from datetime import datetime


def create_trip(user_id, trip_data):
    collection = trips_collection()

    trip = {
        "user_id": user_id,
        "trip": trip_data,
        "created_at": datetime.utcnow(),
    }

    collection.insert_one(trip)
    return trip


def get_user_trips(user_id):
    collection = trips_collection()
    return list(collection.find({"user_id": user_id}))
