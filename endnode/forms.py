from django import forms
from .models import *


class EndNodeAddForm(forms.ModelForm):
    class Meta:
        model = EndNode

        fields = [
            "name",
            "date",
            "description",
            "altitude",
            "latitude",
            "node_status",
        ]