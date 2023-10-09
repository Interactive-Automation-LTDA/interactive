from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ManufacturerForm, SupplierForm, MaterialForm, UserSignupForm, UserLoginForm
from .models import *
from django.http import JsonResponse
import json


def home(request):

    return render(request, "cpq/home.html")


def signup(request):
    form = UserSignupForm()
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username):
            messages.error(request, "Este usuário já existe!")
            
        
        if User.objects.filter(email=email):
            messages.error(request, "Este email já existe!")
            

        if len(username) < 10:
            messages.error(request, "Nome de usuário necessita ter ao mínimo dez caracteres!")
            

        if not username.isalnum():
            messages.error(request, "Nome de usuário precisa ser alpha numérico!")
            
        else:

            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()

            messages.success(request, "Usuário criado com sucesso!")
    
    context = {"form": form}
    return render(request, "cpq/signup.html", context)


def signin(request):
    form = UserLoginForm()
    if request.method=="POST" :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            first_name = user.first_name
            context = {"first_name": first_name}
            return render(request, 'cpq/home.html', context)
        else:
            messages.error(request, "Usuário  inválido")
        
    
    context = {"form": form}
    return render(request, 'cpq/signin.html', context)


def signout(request):
    logout(request)
    return  redirect('signin')


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


def cart(request):

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, "cpq/cart.html", context)


def checkout(request):

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'cpq/checkout.html', context)


def material_list(request):
    materials = Material.objects.all().order_by('name')
    context = {"materials": materials}
    return render(request, "cpq/material_list.html", context)


def material_update(request):
    data = json.loads(request.body)
    product_id = data['productID']
    action = data['action']
    
    print(f"'product_id:'{product_id}, 'action': {action}")

    customer = request.user.customer
    material = Material.objects.get(id=product_id)
    
    return JsonResponse("Material Update View", safe=False)