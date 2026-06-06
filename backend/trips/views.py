from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from users.services import get_or_create_user
from .services import create_trip, get_user_trips
from ai_engine.trip_generator import generate_trip_itinerary


def health_check(request):
    return JsonResponse({
        "status": "ok",
        "service": "ai travel planner backend"
    })


def protected_test(request):
    if not request.firebase_user:
        return JsonResponse(
            {"error": "Authentication required"},
            status=401
        )

    return JsonResponse({
        "message": "Authentication request successful",
        "user": request.firebase_user.get("email")
    })


@csrf_exempt
def create_trip_view(request):
    if not request.firebase_user:
        return JsonResponse(
            {"error": "Authentication required"},
            status=401
        )

    user = get_or_create_user(request.firebase_user)
    data = json.loads(request.body)

    trip = create_trip(user["_id"], data)

    return JsonResponse({
        "message": "Trip created"
    })


def list_trips_view(request):
    if not request.firebase_user:
        return JsonResponse(
            {"error": "Authentication required"},
            status=401
        )

    user = get_or_create_user(request.firebase_user)
    trips = get_user_trips(user["_id"])

    serialized_trips = []

    for t in trips:
        serialized_trips.append({
            "_id": str(t["_id"]),
            "user_id": str(t["user_id"]),
            "trip": t.get("trip"),
            "created_at": t["created_at"].isoformat()
            if "created_at" in t else None
        })

    return JsonResponse({
        "trips": serialized_trips
    })


@csrf_exempt
def generate_ai_trip_view(request):
    if not request.firebase_user:
        return JsonResponse(
            {"error": "Authentication required"},
            status=401
        )

    try:
        user = get_or_create_user(request.firebase_user)
        data = json.loads(request.body)

        destination = data.get("destination")
        days = data.get("days")
        budget = data.get("budget")
        preferences = data.get("preferences", [])

        ai_response = generate_trip_itinerary(
            destination,
            days,
            budget,
            preferences
        )

        if isinstance(ai_response, dict):
            itinerary = ai_response

        else:
            cleaned = ai_response.strip()

            if cleaned.startswith("```"):
                cleaned = cleaned.replace("```json", "")
                cleaned = cleaned.replace("```", "")
                cleaned = cleaned.strip()

            itinerary = json.loads(cleaned)

        create_trip(user["_id"], itinerary)

        return JsonResponse({
            "message": "AI trip generated successfully",
            "itinerary": itinerary
        })

    except Exception as e:
        return JsonResponse({
            "error": "AI_GENERATION_ERROR",
            "type": type(e).__name__,
            "message": str(e)
        }, status=500)