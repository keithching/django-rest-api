from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    provider = serializers.CharField(source='provider.name')
    category = serializers.CharField(source='category.name')
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='event-detail',
        lookup_field='pk'
    )
    class Meta:
        model = Event
        fields = [
            'url',
            'edit_url',
            'pk',
            'title',
            'provider',
            'category',
            'location',
            'date_start',
            'date_end'
        ]
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("event-edit", kwargs={"pk": obj.pk}, request=request)