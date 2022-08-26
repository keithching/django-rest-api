from rest_framework.routers import DefaultRouter

from eventproviders.viewsets import EventProviderGenericViewSet

router = DefaultRouter()
router.register('eventproviders-abc', EventProviderGenericViewSet, basename='eventproviders')

urlpatterns = router.urls