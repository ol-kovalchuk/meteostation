from django.urls import path
from . import views

urlpatterns = [
    path("readings/", views.readings),
    path("latest/", views.latest_reading),
]
