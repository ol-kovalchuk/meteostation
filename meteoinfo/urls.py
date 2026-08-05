from django.urls import path
from .views import all_readings, home

urlpatterns = [
    path("", home, name="home"),
    path("all/", all_readings, name="all_readings"),
]
