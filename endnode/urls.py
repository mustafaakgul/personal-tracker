from django.urls import path
from . import views


app_name = "endnode"


urlpatterns = [
    path("new-endnode/", views.addEndNode, name = "addEndNode"),
]