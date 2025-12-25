from django.shortcuts import render
from django.http import JsonResponse

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