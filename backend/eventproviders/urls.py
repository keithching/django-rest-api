from django.urls import path

from . import views

urlpatterns = [
    path('', views.eventprovider_list_create_view, name="eventprovider-list"),
    path('<int:pk>/update/', views.eventprovider_update_view, name="eventprovider-edit"),
    path('<int:pk>/delete/', views.eventprovider_destroy_view),
    path('<int:pk>/', views.eventprovider_detail_view, name="eventprovider-detail")
]