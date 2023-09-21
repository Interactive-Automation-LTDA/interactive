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
    STATE = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), 
        ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), 
        ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), 
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), 
        ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), 
        ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]
    state = forms.ChoiceField(choices=STATE)

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