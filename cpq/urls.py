from django.urls import path
from cpq.views import *


app_name = 'cpq'

urlpatterns = [
    path('manufacturer_list/', manufacturer_list, name='manufacturer_list'),
    path('manufacturer_insert/', manufacturer_insert, name='manufacturer_insert'),
    path('supplier_insert/', supplier_insert, name='supplier_insert'),
    path('supplier_list/', supplier_list, name='supplier_list'),
    path('material_insert/', material_insert, name='material_insert'),
]