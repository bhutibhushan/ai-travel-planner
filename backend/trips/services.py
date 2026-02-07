from common.db import trips_collection
from datetime import datetime


def create_trip(user_id, trip_data):
    collection = trips_collection()

    trip = {
        "user_id": str(user_id),
        "trip": trip_data,
        "created_at": datetime.utcnow(),
    }

    result = collection.insert_one(trip)

    print("INSERT SUCCESSFUL:", result.inserted_id)

    return trip




def get_user_trips(user_id):
    collection = trips_collection()
    return list(collection.find())
