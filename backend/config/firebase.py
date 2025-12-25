import firebase_admin
from firebase_admin import credentials
from django.conf import settings
import os

def initialize_firebase():
    if not firebase_admin._apps:
        cred_path = os.path.join(
            settings.BASE_DIR,
            'config',
            'firebase_service_account.json'
        )
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)