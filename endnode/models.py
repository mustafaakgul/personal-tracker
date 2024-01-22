from django.db import models
from django.conf import settings


status = [
    ("active", "Active"),
    ("passive", "Passive")
]


class EndNode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userEndnode")
    name = models.CharField(max_length=40)
    date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=100)
    altitude = models.IntegerField()
    latitude = models.IntegerField()
    node_status = models.CharField(max_length=10, choices=status)
    node_last_data_received = models.DateTimeField(max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
