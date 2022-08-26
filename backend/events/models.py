from django.db import models

from eventproviders.models import EventProvider
from eventcategories.models import EventCategory

class Event(models.Model):
    title = models.CharField(max_length=32, unique=True, blank=False)
    provider = models.ForeignKey(EventProvider, on_delete=models.CASCADE, related_name="providers")
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name="categories")
    location = models.CharField(max_length=32, blank=False)
    date_start = models.DateTimeField(blank=False)
    date_end = models.DateTimeField(blank=False)

    def __str__(self):
        return f"{self.id}: [{self.category}]{self.title} in {self.location}"
