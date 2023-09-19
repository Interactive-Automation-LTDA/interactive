from django import forms
from django.forms import ModelForm
from .models import Manufacturer, Supplier, Material

class ManufacturerForm(ModelForm):
    name = forms.CharField()
    cnpj = forms.CharField()

    class Meta:
        model = Manufacturer
        fields = ['name', 'cnpj']



class SupplierForm(ModelForm):
    name = forms.CharField()
    cnpj = forms.CharField()

    class Meta:
        model = Supplier
        fields = ['name', 'cnpj']


class MaterialForm(ModelForm):
    ncm_code = forms.IntegerField()
    material_code = forms.IntegerField()
    name = forms.CharField()
    description = forms.TimeField()
    unit = forms.CharField()
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all())
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all())
    state = forms.CharField()

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