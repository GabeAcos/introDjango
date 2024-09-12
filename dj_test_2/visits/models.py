from django.db import models


class Visits(models.Model):
    page = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, default="anonymous")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visits {self.pk}"
