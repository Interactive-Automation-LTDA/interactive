from django.urls import path
from cpq.views import *

urlpatterns = [
    path('', material_list, name='material_list'),
]