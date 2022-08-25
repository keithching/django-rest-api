import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from eventproviders.models import EventProvider
from eventproviders.serializers import EventProviderSerializer

# testing the return of HttpResponse to the client
def index(request):
    return JsonResponse({"message": "Fish"})

def http_response_test(request):
    data = {"message": "Fish"}
    json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers={"content-type": "application/json"})

# a django view that returns JSON data written with pure django and JsonResponse
def json_response_test(request):
    # request -> HttpRequest -> Django
    body = request.body # byte string of JSON data
    data = {}
    try: 
        data = json.loads(body) # string of JSON data -> Python dict
    except:
        pass

    data['params'] = dict(request.GET) # url query param
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data) 
    '''
    JsonResponse do not automatically grab stuff like the request header and content type
    and echo back to the client
    '''

# a django view that returns JSON data written with pure django and JsonResponse
def event_provider(request):
    # model instance (provider)
    # turn a Python dict
    # return JSON to my client
    provider = EventProvider.objects.first()
    data = {}
    if provider:
        data = model_to_dict(provider, fields=['id', 'name'])
        # data['id'] = provider.id
        # data['name'] = provider.name
        # data['email'] = provider.email
        # data['date_reg'] = provider.date_reg

        # serialization
    return JsonResponse(data)

# an API view with django rest framework
# @api_view(["GET", "POST"])
# def event_provider_rest(request):
#     provider = EventProvider.objects.first()
#     data = {}
#     if provider:
#         data = model_to_dict(provider, fields=['id', 'name'])
#         # next step - use a custom serializer within the rest framework instead of using model_to_dict
#     return Response(data)

# with model serializer
# @api_view(["GET", "POST"])
# def event_provider_rest(request):
#     instance = EventProvider.objects.first()
#     data = {}
#     if instance:
#         data = EventProviderSerializer(instance).data
#         # it does:
#             # the model_to_dict stuff
#             # it can enrich the data that is coming through the serializer in a clear way
#             # it validates the data that is coming through
#     return Response(data)


@api_view(["POST"])
def event_provider_rest(request):
    serializer = EventProviderSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): # verify the validation of data coming through
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)

