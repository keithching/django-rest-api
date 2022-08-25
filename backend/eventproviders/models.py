from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from django.utils import timezone

class EventProvider(models.Model):
    # Primary keys (IDs) are added automatically. (You can override this, too.)
    name = models.CharField(max_length=32, unique=True, blank=False)
    email = models.CharField(max_length=32, unique=True, blank=False)
    date_reg = models.DateTimeField('date registered', default=timezone.now)
    # password not to be saved in the DB

    def __str__(self): # string representation for this model
        return f"{self.id}: {self.name}"
    
    def greet(self):
        return f"Hello {self.name}!"

class EventCategory(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    date_reg = models.DateTimeField('date registered', default=timezone.now)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Event(models.Model):
    title = models.CharField(max_length=32, unique=True, blank=False)
    provider = models.ForeignKey(EventProvider, on_delete=models.CASCADE)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    location = models.CharField(max_length=32, blank=False)
    date_start = models.DateTimeField(blank=False)
    date_end = models.DateTimeField(blank=False)

    def __str__(self):
        return f"{self.id}: [{self.category}]{self.title} in {self.location}"