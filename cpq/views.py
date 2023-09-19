from django.shortcuts import render
from .forms import ManufacturerForm
from .models import *
# Create your views here.

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    context = {"manufacturers": manufacturers}
    return render(request, 'cpq/manufacture_list.html', context)

def manufacturer_insert(request):
    if request.method == "POST" :
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": ManufacturerForm}
    return render(request, 'cpq/manufacture_insert.html', context)