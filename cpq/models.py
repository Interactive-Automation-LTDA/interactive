from django.db import models
from cpq.utils import formatters, validators

validator = validators.Validator()

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)


    def __str__(self) -> str:
        return self.name

    @property
    def formated_cpf_cnpj(self):
        return formatters.cpf_cnpj(self.cnpj)

    @formated_cpf_cnpj.setter
    def cpf_cnpj_formated(self, value):
        validator.cpf_cnpj_validator(value)
        self.cnpj = validator.mask_number_removal(value)


class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)


    def __str__(self) -> str:
        return self.name

    @property
    def formated_cpf_cnpj(self):
        return formatters.cpf_cnpj(self.cnpj)
    
    @formated_cpf_cnpj.setter
    def cpf_cnpj_formated(self, value):
        validator.cpf_cnpj_validator(value)
        self.cnpj = validator.mask_number_removal(value)
        

class Material(models.Model):
    ncm_code = models.IntegerField()
    material_code = models.IntegerField()
    name = models.CharField(max_length=55)
    description = models.TextField()
    unit = models.CharField(max_length=55)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    STATE = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), 
        ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), 
        ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), 
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), 
        ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), 
        ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]

    state = models.CharField(max_length=30, choices=STATE)

    def __str__(self) -> str:
        return self.name