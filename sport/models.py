from django.db import models
from django.conf import settings


class Bike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userBike")
    bike_note = models.CharField(max_length=20, blank=True, null=True)
    bike_date = models.DateTimeField()
    bike_time = models.CharField(max_length=5)
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.bike_date} {self.bike_note}'
