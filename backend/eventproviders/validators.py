from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import EventProvider

# but if the validation has already been covered in the Django Model, this extra validator might not be needed
# def validate_name(value):
#     qs = EventProvider.objects.filter(name__iexact=value) # iexact: case insensitive
#     if qs.exists():
#         raise serializers.ValidationError(f"{value} is already a event provider name.")
#     return value

# say we don't allow hello to exist in the event provider name
def validate_name_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} is not allowed")
    return value

# a unique validator for the event provider name (for demonstration purpose)
unique_eventprovider_name = UniqueValidator(queryset=EventProvider.objects.all(), lookup='iexact')