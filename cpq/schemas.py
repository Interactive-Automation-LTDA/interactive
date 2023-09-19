from ninja import Schema


class CreateManufacturerSchema(Schema):
    name: str
    cnpj: str


class CreateSupplierSchema(Schema):
    name: str
    cnpj: str


class CreateMateialSchema(Schema):
    ncm_code: int
    material_code: int
    name: str
    description: str
    unit: str
    manufacturer: str
    supplier: str
    state: str