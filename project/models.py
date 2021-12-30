from django.db import models
from django.conf import settings


status = [
    ("active", "Aktif"),
    ("done", "Tamamlandı")
]


class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userProject")
    name = models.CharField(max_length=40)
    date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=100)
    project_status = models.CharField(max_length=10, choices=status)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name
