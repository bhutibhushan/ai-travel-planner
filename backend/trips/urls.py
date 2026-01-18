from django.urls import path
from .views import health_check,protected_test,create_trip_view,list_trips_view

urlpatterns=[
    path('health/',health_check,name='health_check'),
    path('protected/',protected_test),
    path('create/',create_trip_view),
    path('list/',list_trips_view),
]