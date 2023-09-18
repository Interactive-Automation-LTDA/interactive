from ninja import Router
from typing import List
from .models import Manufacturer, Supplier, Material

from ninja.orm import create_schema


router = Router()


ManufacturerSchema = create_schema(Manufacturer)
SupplierSchema = create_schema(Supplier)
MaterialSchema = create_schema(Material)


@router.post('manufacturer/', response={201: ManufacturerSchema})
def create_manufacture(request, payload: ManufacturerSchema):
    query_set = Manufacturer.objects.create(**payload.dict())
    return 201, query_set


@router.get('manufactuter/', response=List[ManufacturerSchema])
def get_all_manufacuters(request):
    query_set = Manufacturer.objects.all()
    return query_set


@router.post('supplier/')
def create_supplier(request, payload: SupplierSchema):
    query_set = Manufacturer.objects.create(**payload.dict())
    return {"nome": query_set.name}


@router.post('material/')
def create_material(request, payload: MaterialSchema):
    query_set = Material.objects.create(**payload.dict())
    return {"nome": query_set.name}
