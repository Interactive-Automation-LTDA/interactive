from django.urls import path
from django.contrib.auth import views as auth
from .views import *


app_name = 'cpq'

urlpatterns = [
    path('home/', home, name='home'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', auth.LogoutView.as_view(template_name ='cpq/home.html'), name ='logout'),
    path('manufacturer_list/', manufacturer_list, name='manufacturer_list'),
    path('manufacturer_insert/', manufacturer_insert, name='manufacturer_insert'),
    path('supplier_insert/', supplier_insert, name='supplier_insert'),
    path('supplier_list/', supplier_list, name='supplier_list'),
    path('material_insert/', material_insert, name='material_insert'),
    path('material_list/', material_list, name='material_list'),
    path('material_update/', material_update, name='material_update'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]