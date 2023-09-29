from django import forms
from django.forms import ModelForm
from .models import Manufacturer, Supplier, Material

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
            'manufacturer',
            'supplier',
            'state'
            ]