from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='user_list_create_view'),
    path('users/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_view'),
]