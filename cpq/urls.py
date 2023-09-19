from django.urls import path
from cpq.views import *

urlpatterns = [
    path('manufacturer_list/', manufacturer_list, name='manufacturer_list'),
    path('manufacturer_insert/', manufacturer_insert, name='manufacturer_insert'),
]