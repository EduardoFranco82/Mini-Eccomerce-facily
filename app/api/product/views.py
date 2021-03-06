from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from .schemas import ProductSchema, ShowProductSchema
from app.models.models import Product, User
from app.repositories.product_repository import ProductRepository
from app.services.auth_service import get_user, only_admin
from fastapi.exceptions import HTTPException

router = APIRouter(dependencies=[Depends(only_admin)])

# --> estrutura padrão para todas as rotas que chamar a router
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product: ProductSchema, repository: ProductRepository = Depends()): # --> db: Session = Depends(get_db) --> abre uma sessao com o banco no arquivo db.py
   return repository.create(Product(**product.dict()))


@router.get('/', response_model=List[ShowProductSchema]) # --> 
def index(repository: ProductRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, product: ProductSchema, repository: ProductRepository = Depends()):
   return repository.update(id, product.dict())

@router.get('/{id}', response_model=ShowProductSchema)
def show(id: int, repository: ProductRepository = Depends()):
    return repository.get_by_id(id) # --> faz a busca atraves do id
