from django import forms
from .models import *


class BikeAddForm(forms.ModelForm):
    class Meta:
        model = Bike

        fields = [
            "bike_note",
            "bike_date",
            "bike_time",
        ]