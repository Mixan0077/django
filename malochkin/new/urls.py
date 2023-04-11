from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.clients, name='clients'),
    path('', views.izdelie_list, name='izdelie_list'),
    path('izdelie/<int:pk>/', views.izdelie_detail, name='izdelie_detail'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]