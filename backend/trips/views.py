from django.shortcuts import render
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({
        "status":"ok",
        "service":"ai travel planner backend"
    })