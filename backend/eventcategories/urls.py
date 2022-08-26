from django.urls import path

from . import views

urlpatterns = [
    path('', views.eventcategory_list_create_view),
    path('<int:pk>/update/', views.eventcategory_update_view),
    path('<int:pk>/delete/', views.eventcategory_destroy_view),
    path('<int:pk>/', views.eventcategory_detail_view)
]