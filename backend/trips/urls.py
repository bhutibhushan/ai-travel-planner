from django.urls import path
from .views import health_check,protected_test

urlpatterns=[
    path('health/',health_check,name='health_check'),
    path('protected/',protected_test)
]