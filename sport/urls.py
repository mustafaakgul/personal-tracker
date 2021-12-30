from django.urls import path
from . import views


app_name = "sport"


urlpatterns = [
    path("new-bike-entry/", views.addBike, name = "addBike"),
]