from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contact, name='contacts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
