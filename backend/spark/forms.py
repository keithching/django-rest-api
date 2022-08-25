# demonstration purpose between django forms and rest framework serializers only
from django import forms
from .models import EventProvider

class EventProviderForm(forms.ModelForm):
    class Meta:
        model = EventProvider
        fields = [
            'name',
            'email',
            'date_reg'
        ]