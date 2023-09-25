from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Manufacturer, Supplier, Material

class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = ['name', 'cnpj']

    def clean_name(self):
        manufacturer_name = self.cleaned_data.get('name')
        for instance in Manufacturer.objects.all():
            if instance.name == manufacturer_name:
                raise ValidationError(f'O Fabricante {instance.name} já existe')
        return manufacturer_name
    
        # manufacturer_name = self.cleaned_data.get('name')
        # manufacturer_cnpj = self.cleaned_data.get('cnpj')
        # for instance in Manufacturer.objects.all():
        #     if instance.name == manufacturer_name or instance.cnpj == manufacturer_cnpj:
        #         print(f'Esse fabricante: {instance.name} e CNPJ: {instance.cnpj} já existem.')


    

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