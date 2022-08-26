from django.urls import path

from . import views

urlpatterns = [
    path('', views.event_list_create_view, name='event-list'),
    path('<int:pk>/update/', views.event_update_view, name='event-edit'),
    path('<int:pk>/delete/', views.event_destroy_view),
    path('<int:pk>/', views.event_detail_view, name='event-detail')
]