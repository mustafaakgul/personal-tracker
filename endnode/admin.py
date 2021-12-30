from django.contrib import admin
from .models import EndNode


@admin.register(EndNode)
class EndNodeAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'date',
        'description',
        'altitude',
        'latitude',
        'node_status',
        'node_last_data_received'
        ]