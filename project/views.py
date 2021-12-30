from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProjectAddForm
from django.contrib import messages


@login_required(login_url= "accounts:authentication")
def addProject(request):
    projectForm = ProjectAddForm(request.POST or None)
    context = {
        "projectForm" : projectForm
    }

    if projectForm.is_valid():
        projectModel = projectForm.save(commit=False)
        print(projectModel)
        projectModel.user = request.user
        projectModel.save()
        messages.success(request, "Project entry added.")

    return render(request, "project/project-add.html", context)