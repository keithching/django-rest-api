from django.db import models
from django.utils import timezone

class EventProvider(models.Model):
    # Primary keys (IDs) are added automatically by default
    name = models.CharField(max_length=32, unique=True, blank=False)
    email = models.CharField(max_length=32, unique=True, blank=False)
    date_reg = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self): # string representation for this model
        return f"{self.id}: {self.name}"
    
    def greet(self):
        return f"Hello {self.name}!"