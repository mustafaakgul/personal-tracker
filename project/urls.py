from django.urls import path
from . import views


app_name = "project"


urlpatterns = [
    path("new-project/", views.addProject, name = "addProject"),
]