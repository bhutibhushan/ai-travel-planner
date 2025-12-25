from django.http import JsonResponse
from .firebase_auth import verify_firebase_token


class FirebaseAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            request.firebase_user = None
            return self.get_response(request)

        if not auth_header.startswith("Bearer "):
            return JsonResponse(
                {"error": "Invalid authorization header format"},
                status=401
            )

        token = auth_header.replace("Bearer ", "").strip()

        try:
            decoded_token = verify_firebase_token(token)
            request.firebase_user = decoded_token
        except Exception:
            return JsonResponse(
                {"error": "Invalid or expired token"},
                status=401
            )

        return self.get_response(request)
