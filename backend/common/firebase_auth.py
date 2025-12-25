import os
import firebase_admin
from firebase_admin import auth, credentials
from django.conf import settings


def initialize_firebase_if_needed():
    if not firebase_admin._apps:
        cred_path = os.path.join(
            settings.BASE_DIR,
            'config',
            'firebase_service_account.json'
        )
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)


def verify_firebase_token(id_token):
    initialize_firebase_if_needed()
    return auth.verify_id_token(id_token)
