from django.shortcuts import render
from django.http import JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt
from users.services import get_or_create_user
from .services import create_trip,get_user_trips

def health_check(request):
    return JsonResponse({
        "status":"ok",
        "service":"ai travel planner backend"
    })

def protected_test(request):
    if not request.firebase_user:
        return JsonResponse(
            {"error":"Authentication required"},
            status=401
        )

    return JsonResponse({
        "message":"Authentication request successful",
        "user": request.firebase_user.get("email")
    })

@csrf_exempt
def create_trip_view(request):
    if not request.firebase_user:
        return JsonResponse({"error": "Authentication required"},status=401)

    user = get_or_create_user(request.firebase_user)
    data = json.loads(request.body)

    trip = create_trip(user["_id"],data)

    return JsonResponse({"message": "Trip created"})

def list_trips_view(request):
    if not request.firebase_user:
        return JsonResponse({"error": "Authentication required"}, status=401)

    user = get_or_create_user(request.firebase_user)
    trips = get_user_trips(user["_id"])

    serialized_trips = []

    for t in trips:
        serialized_trips.append({
            "_id": str(t["_id"]),
            "user_id": str(t["user_id"]),
            "trip": t.get("trip"),
            "created_at": t["created_at"].isoformat() if "created_at" in t else None
        })

    return JsonResponse({"trips": serialized_trips})

