from django.db import models
from django.utils import timezone

class EventCategory(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    date_reg = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return f"{self.id}: {self.name}"
