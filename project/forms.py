from django import forms
from .models import *


class ProjectAddForm(forms.ModelForm):
    class Meta:
        model = Project

        fields = [
            "name",
            "date",
            "description",
            "project_status"
        ]