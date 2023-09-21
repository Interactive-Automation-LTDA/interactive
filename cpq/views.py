from django.shortcuts import render, redirect
from django.http import Http404
from .forms import ManufacturerForm, SupplierForm, MaterialForm
from .models import *
# Create your views here.


def manufacturer_insert(request):
    manufacturer_form_data = request.session.get('manufacturer_form_data', None)
    # if request.method == "POST" :
    #     form = ManufacturerForm(manufacturer_form_data)
    #     if form.is_valid():
    #         form.save()
    # else:
    form = ManufacturerForm(manufacturer_form_data)

    context = {"form": form}
    return render(request, 'cpq/manufacture_insert.html', context)


def manufacturer_created(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['manufacturer_form_data'] = POST
    form = ManufacturerForm(request.POST)

    return redirect('cpq:manufacturer_insert')


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all().order_by('name')
    context = {"manufacturers": manufacturers}
    return render(request, 'cpq/manufacture_list.html', context)


def supplier_insert(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierForm()
    
    context = {"form": form}
    return render(request, 'cpq/supplier_insert.html', context)


def supplier_list(request):
    suppliers = Supplier.objects.all().order_by('name')
    context = {"suppliers": suppliers}
    return render(request, 'cpq/supplier_list.html', context)


def material_insert(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MaterialForm()

    context = {"form": form}
    return render(request, 'cpq/material_insert.html', context)