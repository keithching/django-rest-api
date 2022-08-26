from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import EventProvider
from .validators import validate_name_no_hello, unique_eventprovider_name

class EventProviderSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='eventprovider-detail',
        lookup_field='pk'
    )
    name = serializers.CharField(validators=[validate_name_no_hello, unique_eventprovider_name])
    # we can add in arbituary fields
    # say if we want to send an email to this address whether a new event provider is created
    # emailToSend = serializers.EmailField(write_only=True)
    class Meta:
        model = EventProvider
        fields = [
            'url',
            'edit_url',
            'pk',
            # 'emailToSend',
            'name',
            'email',
            'date_reg'
        ]
    
    # an inline way of validating data in the serializer before saving it
    # this example ensures the title is unique (case insensitive)
    # the other way is through the validators.py

    # def validate_name(self, value):
    #     qs = EventProvider.objects.filter(name__iexact=value) # iexact: case insensitive
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a event provider name.")
    #     return value

    # def create(self, validated_data):
    #     # return EventProvider.objects.create(**validated_data)
    #     emailToSend = validated_data.pop('emailToSend') # remove the email field from the validated data before creating it in the django model
    #     obj = super().create(validated_data)
    #     print(emailToSend, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     emailToSend = validated_data.pop('emailToSend')
    #     return super().update(instance, validated_data)

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