from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import EventCategory

class EventCategorySerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='eventcategory-detail',
        lookup_field='pk'
    )
    class Meta:
        model = EventCategory
        fields = [
            'url',
            'edit_url',
            'pk',
            'name',
            'date_reg'
        ]
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("eventcategory-edit", kwargs={"pk": obj.pk}, request=request)