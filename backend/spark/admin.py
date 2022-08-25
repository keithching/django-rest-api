from django.contrib import admin

# Register your models here.
from eventproviders.models import EventProvider, EventCategory, Event

admin.site.register(EventProvider)
admin.site.register(EventCategory)
admin.site.register(Event)