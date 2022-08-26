from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    provider = serializers.CharField(source='provider.name')
    category = serializers.CharField(source='category.name')
    class Meta:
        model = Event
        fields = [
            'title',
            'provider',
            'category',
            'location',
            'date_start',
            'date_end'
        ]