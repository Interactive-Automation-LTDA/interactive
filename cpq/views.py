from django.shortcuts import render
from django.contrib import messages
from .forms import ManufacturerForm, SupplierForm, MaterialForm
from .models import *


def manufacturer_insert(request):
    form = ManufacturerForm()  
    if request.method == "POST":
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Fabricante: {form.data['name']} cadastrado com sucesso!")
        else:
            messages.warning(request, f"Fabricante: {form.data['name']} e CNPJ: {form.data['cnpj']} já cadastrados")

    context = {"form": form}
    return render(request, "cpq/manufacturer_insert.html", context)


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all().order_by("name")
    context = {"manufacturers": manufacturers}
    return render(request, "cpq/manufacturer_list.html", context)


def supplier_insert(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierForm()
    
    context = {"form": form}
    return render(request, "cpq/supplier_insert.html", context)


def supplier_list(request):
    suppliers = Supplier.objects.all().order_by("name")
    context = {"suppliers": suppliers}
    return render(request, "cpq/supplier_list.html", context)


def material_insert(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MaterialForm()

    context = {"form": form}
    return render(request, "cpq/material_insert.html", context)