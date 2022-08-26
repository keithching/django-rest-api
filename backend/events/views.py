from rest_framework import generics, mixins, authentication, permissions
from .models import Event
from .serializers import EventSerializer
from spark.mixins import StaffEditorPermissionMixin

class EventListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

event_list_create_view = EventListCreateAPIView.as_view()

class EventDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView): 
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    # lookup_field = 'pk'

event_detail_view = EventDetailAPIView.as_view()

class EventUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView): 
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    lookup_field = 'pk'

event_update_view = EventUpdateAPIView.as_view()

class EventDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView): 
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    lookup_field = 'pk'

event_destroy_view = EventDestroyAPIView.as_view()