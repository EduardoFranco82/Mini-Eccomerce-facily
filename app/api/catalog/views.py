from fastapi import APIRouter
from fastapi.params import Depends
from fastapi_pagination import Page

from app.repositories.product_repository import ProductRepository
from .schemas import CatalogFilter,ShowProductSchema

router = APIRouter()

@router.get('/', response_model= Page [ShowProductSchema])
def index(filter : CatalogFilter = Depends(), product_repository : ProductRepository = Depends()):# se eu nao ponho nada nos parametros, ele ja entende por query string
    return product_repository.get_for_catalog(filter)