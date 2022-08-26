from rest_framework import generics, mixins, authentication, permissions
from .models import EventCategory
from spark.mixins import StaffEditorPermissionMixin
from .serializers import EventCategorySerializer
# from .permissions import IsStaffEditorPermission

class EventCategoryListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

eventcategory_list_create_view = EventCategoryListCreateAPIView.as_view()

class EventCategoryDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView): 
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    # lookup_field = 'pk'

eventcategory_detail_view = EventCategoryDetailAPIView.as_view()

class EventCategoryUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView): 
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    lookup_field = 'pk'

eventcategory_update_view = EventCategoryUpdateAPIView.as_view()

class EventCategoryDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView): 
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    lookup_field = 'pk'

eventcategory_destroy_view = EventCategoryDestroyAPIView.as_view()