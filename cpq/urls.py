from django.urls import path
from cpq.views import *

urlpatterns = [
    path('', manufacture_list, name='manufacture_list'),
]