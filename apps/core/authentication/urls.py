from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.ListCreateUserList.as_view(), name='list_create_user_list'),
    path('users/<int:pk>/', views.RetrieveUpdateDestroyUserDetail.as_view(), name='retrieve_update_user_details'),
]