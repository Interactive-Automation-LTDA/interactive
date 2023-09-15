from django_cpf_cnpj.fields import CNPJField
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField('Nome', max_length=100)
    cnpj = CNPJField(masked=True)

    def __str__(self) -> str:
        return self.name


class Supplier(models.Model):
    name = models.CharField('Nome', max_length=100)
    cnpj = CNPJField(masked=True)

    def __str__(self) -> str:
        return self.name


class Material(models.Model):
    ncm_code = models.IntegerField()
    material_code = models.IntegerField()
    name = models.CharField(max_length=55)
    description = models.TextField()
    unit = models.CharField(max_length=55)
    image = models.ImageField()
    manufacturer = models.ForeignKey(Manufacturer)
    supplier = models.ForeignKey(Supplier)

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