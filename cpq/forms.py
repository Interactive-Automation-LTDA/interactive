from django import forms
from django.forms import ModelForm
from .models import Manufacturer, Supplier, Material, Machine
from django.contrib.auth.models import User


class UserLoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserSignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = ['name', 'cnpj']


class SupplierForm(ModelForm):

    class Meta:
        model = Supplier
        fields = ['name', 'cnpj']


class MaterialForm(ModelForm):

    class Meta:
        model = Material
        fields = [
            'ncm_code',
            'material_code',
            'name',
            'description',
            'unit',
            'price',
            'manufacturer',
            'supplier',
            'state'
            ]
        

class MachineForm(ModelForm):

    class Meta:
        model = Machine
        fields = ['name', 'manufacturer', 'supplier', 'material']