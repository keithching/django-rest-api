from rest_framework import mixins, viewsets

from .models import EventProvider
from .serializers import EventProviderSerializer

class EventProviderViewSet(viewsets.ModelViewSet):
    '''
    HTTP get -> list -> Queryset
    get -> retrieve -> Event Provider Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial update
    delete -> destroy
    '''
    queryset = EventProvider.objects.all()
    serializer_class = EventProviderSerializer
    lookup_field = 'pk' # default

class EventProviderGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Event Provider Instance Detail View
    '''
    queryset = EventProvider.objects.all()
    serializer_class = EventProviderSerializer
    lookup_field = 'pk' # default

# these can be used in urls.py to reference to these specific views
# eventprovider_list_view = EventProviderGenericViewSet.as_view({'get': 'list'})
# eventprovider_detail_view = EventProviderGenericViewSet.as_view({'get': 'retrieve'})