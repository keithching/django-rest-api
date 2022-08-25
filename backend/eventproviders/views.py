from rest_framework import generics

from .models import EventProvider
from .serializers import EventProviderSerializer

# this API view can perform both listing and creating, depending on the HTTP request method 
class EventProviderListCreateAPIView(generics.ListCreateAPIView):
    queryset = EventProvider.objects.all()
    serializer_class = EventProviderSerializer

    # def perform_create(self, serializer):

eventprovider_list_create_view = EventProviderListCreateAPIView.as_view()

# django rest framework generic views
class EventProviderDetailAPIView(generics.RetrieveAPIView): 
    queryset = EventProvider.objects.all()
    serializer_class = EventProviderSerializer
    # lookup_field = 'pk'

eventprovider_detail_view = EventProviderDetailAPIView.as_view()

class EventProviderUpdateAPIView(generics.UpdateAPIView): 
    queryset = EventProvider.objects.all()
    serializer_class = EventProviderSerializer
    lookup_field = 'pk'

    # def perform_update(self, serializer):

eventprovider_update_view = EventProviderUpdateAPIView.as_view()

class EventProviderDestroyAPIView(generics.DestroyAPIView): 
    queryset = EventProvider.objects.all()
    serializer_class = EventProviderSerializer
    lookup_field = 'pk'

    # def perform_destroy(self, serializer):

eventprovider_destroy_view = EventProviderDestroyAPIView.as_view()

# the following 2 views are combined as the ListCreateAPIView

# class EventProviderListAPIView(generics.ListAPIView): 
#     queryset = EventProvider.objects.all()
#     serializer_class = EventProviderSerializer
#     # lookup_field = 'pk'

# eventprovider_list_view = EventProviderListAPIView.as_view()

# class EventProviderCreateAPIView(generics.CreateAPIView):
#     queryset = EventProvider.objects.all()
#     serializer_class = EventProviderSerializer

# eventprovider_create_view = EventProviderCreateAPIView.as_view()