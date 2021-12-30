from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BikeAddForm
from django.contrib import messages


@login_required(login_url= "accounts:authentication")
def addBike(request):
    bikeForm = BikeAddForm(request.POST or None)
    context = {
        "bikeform" : bikeForm
    }

    if bikeForm.is_valid():
        bikeModel = bikeForm.save(commit=False)
        bikeModel.user = request.user
        bikeModel.save()
        messages.success(request, "Bike entry added.")

    return render(request, "sport/bike-add.html", context)