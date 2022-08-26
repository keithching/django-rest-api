from django.contrib import admin

# Register your models here.
from eventproviders.models import EventProvider
from eventcategories.models import EventCategory
from events.models import Event

admin.site.register(EventProvider)
admin.site.register(EventCategory)
admin.site.register(Event)