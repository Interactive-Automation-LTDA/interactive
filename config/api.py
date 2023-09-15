from ninja import NinjaAPI
from cpq.material_api import router as cpq_router

api = NinjaAPI()
api.add_router('cpq/', cpq_router)