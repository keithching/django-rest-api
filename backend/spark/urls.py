from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("http_response_test/", views.http_response_test, name="http_response_test"),
    path("json_response_test/", views.json_response_test, name="json_response_test"),
    # path("event_providers/", views.event_provider, name="event_providers"),
    path("event_providers_rest/", views.event_provider_rest, name="event_providers_rest"),
]