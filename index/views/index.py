from django.shortcuts import render
from sport.models import Bike
from project.models import Project
from endnode.models import EndNode


def index(request):

    last_data_4_bike = get_last_data_by_date()
    active_project = get_active_project_number()
    active_endnode = get_active_endnode()

    context = {
        "last_data_4_bike" : last_data_4_bike.bike_time,
        "active_project" : active_project,
        "active_endnode" : active_endnode
    }

    return render(request, "main/index.html", context)


def get_last_data_by_date():
    return Bike.objects.latest('bike_date')


def get_active_project_number():
    return Project.objects.filter(project_status="active").count()


def get_active_endnode():
    return EndNode.objects.filter(node_status="active").count()