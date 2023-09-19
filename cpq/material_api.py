from ninja import Router
from typing import List
from .models import Manufacturer, Supplier, Material

from ninja.orm import create_schema
from .schemas import CreateManufacturerSchema, CreateSupplierSchema, CreateMateialSchema

router = Router()


ManufacturerSchema = create_schema(Manufacturer)
SupplierSchema = create_schema(Supplier)
MaterialSchema = create_schema(Material)


@router.post('manufacturer/')
def create_manufacture(request, payload: CreateManufacturerSchema):
    query_set = Manufacturer.objects.create(**payload.dict())
    return query_set


@router.get('manufacturer/')
def get_all_manufacuters(request):
    query_set = Manufacturer.objects.all()
    return List[query_set]


@router.post('supplier/')
def create_supplier(request, payload: CreateSupplierSchema):
    query_set = Manufacturer.objects.create(**payload.dict())
    return query_set


@router.post('material/')
def create_material(request, payload: CreateMateialSchema):
    query_set = Material.objects.create(**payload.dict())
    return query_set
