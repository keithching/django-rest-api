from rest_framework import serializers
from .models import EventProvider

class EventProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventProvider
        fields = [
            'name',
            'email',
            'date_reg'
        ]