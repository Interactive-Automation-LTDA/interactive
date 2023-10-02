from django.shortcuts import render
from django.contrib import messages
from .forms import ManufacturerForm, SupplierForm, MaterialForm, UserSignupForm
from .models import *


def home(request):

    return render(request, "cpq/home.html")


def signup(request):
    form = UserSignupForm()
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Usuário: {form.data['username']} cadastrado com sucesso!")
            form = UserSignupForm()
        else:
            messages.warning(request, f"Este usuário {form.data['username']} já existe!")
    
    context = {"form": form}
    return render(request, "cpq/signup.html", context)


def manufacturer_insert(request):
    form = ManufacturerForm()  
    if request.method == "POST":
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Fabricante: {form.data['name']} cadastrado com sucesso!")
            form = ManufacturerForm()
        else:
            messages.warning(request, f"Fabricante: {form.data['name']} e CNPJ: {form.data['cnpj']} já cadastrados")

    context = {"form": form}
    return render(request, "cpq/manufacturer_insert.html", context)


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all().order_by("name")
    context = {"manufacturers": manufacturers}
    return render(request, "cpq/manufacturer_list.html", context)


def supplier_insert(request):
    form = SupplierForm()
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Fornecedor: {form.data['name']} cadastrado com sucesso!")
            form = SupplierForm()
        else:
            messages.warning(request, f"Fornecedor: {form.data['name']} e CNPJ: {form.data['cnpj']} já cadastrados")
    
    context = {"form": form}
    return render(request, "cpq/supplier_insert.html", context)


def supplier_list(request):
    suppliers = Supplier.objects.all().order_by("name")
    context = {"suppliers": suppliers}
    return render(request, "cpq/supplier_list.html", context)


def material_insert(request):
    form = MaterialForm()
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Material: {form.data['name']} cadastrado com sucesso!")
            form = MaterialForm()
        else:
            messages.warning(request, f"Material: {form.data['name']} e Código: {form.data['material_code']} já cadastrados")

    context = {"form": form}
    return render(request, "cpq/material_insert.html", context)


def material_list(request):
    materials = Material.objects.all().order_by('name')
    context = {"materials": materials}
    return render(request, "cpq/material_list.html", context)