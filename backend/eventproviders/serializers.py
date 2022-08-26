from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import EventProvider

class EventProviderSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='eventprovider-detail',
        lookup_field='pk'
    )
    class Meta:
        model = EventProvider
        fields = [
            'url',
            'edit_url',
            'pk',
            'name',
            'email',
            'date_reg'
        ]
    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("eventprovider-detail", kwargs={"pk": obj.pk}, request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("eventprovider-edit", kwargs={"pk": obj.pk}, request=request)