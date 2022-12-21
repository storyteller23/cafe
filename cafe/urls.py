from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('orders', orders, name='orders'),
    path('create_order', create_order, name='create_order'),
]
