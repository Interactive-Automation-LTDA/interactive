from ninja import Router
from typing import List
from .models import Manufacturer, Supplier, Material

from ninja.orm import create_schema


router = Router()


ManufacturerSchema = create_schema(Manufacturer)
SupplierSchema = create_schema(Supplier)
MaterialSchema = create_schema(Material)


@router.post('manufacturer/')
def create_manufacture(request, payload: ManufacturerSchema):
    query_set = Manufacturer.objects.create(**payload.dict())
    return {"nome": query_set.name}


@router.post('supplier/')
def create_supplier(request, payload: SupplierSchema):
    query_set = Manufacturer.objects.create(**payload.dict())
    return {"nome": query_set.name}


@router.post('material/')
def create_material(request, payload: MaterialSchema):
    query_set = Material.objects.create(**payload.dict())
    return {"nome": query_set.name}
