from multiprocessing import Event
from rest_framework import generics, mixins, authentication, permissions

from .models import EventProvider
from .permissions import IsStaffEditorPermission
from .serializers import EventProviderSerializer

# this API view can perform both listing and creating, depending on the HTTP request method 
class EventProviderListCreateAPIView(generics.ListCreateAPIView):
    queryset = EventProvider.objects.all()
    serializer_class = EventProviderSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] # permission and authentication for this API view

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

# class EventProviderMixinView(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView
#     ):
#     queryset = EventProvider.objects.all()
#     serializer_class = EventProviderSerializer
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs): # HTTP -> get
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs) # this list method comes from mixins.ListModelMixin
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# eventprovider_mixin_view = EventProviderMixinView.as_view()