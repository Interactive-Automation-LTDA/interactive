from django.db import models
from django.contrib.auth.models import User
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
    ncm_code = models.CharField(max_length=55, unique=True)
    material_code = models.CharField(max_length=55, unique=True)
    name = models.CharField(max_length=55, unique=True)
    description = models.TextField()
    unit = models.CharField(max_length=55)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=3)

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
    

class Order(models.Model):
    user = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    

class OrderItem(models.Model):
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0,  null=True,  blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.material.name)
    
    @property
    def get_total(self):
        total  = self.material.price * self.quantity
        return total


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order,  on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)

    STATE = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), 
        ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), 
        ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), 
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), 
        ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), 
        ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]

    state = models.CharField(max_length=30, choices=STATE)
    zip_code = models.CharField(max_length=200,  null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return  str(self.address)
    

class Machine(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    material = models.ManyToManyField(Material)
    price = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self)-> str:
        return str(self.name)