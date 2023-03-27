from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category_list_create_view'),
    path('products/', views.ProductListCreateView.as_view(), name='product_list_create_view'),
]