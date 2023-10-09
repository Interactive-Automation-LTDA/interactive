from django.contrib import admin
from .models import *

admin.site.register(Manufacturer)
admin.site.register(Supplier)
admin.site.register(Material)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)