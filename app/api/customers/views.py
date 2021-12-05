from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from .schemas import CustomersSchema, ShowCustomersSchema
from app.repositories.customers_repository import CustomersRepository
from app.models.models import Customers
from typing import List
router = APIRouter()


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(customer: CustomersSchema, repository: CustomersRepository = Depends()):
    repository.create(Customers(**customer.dict()))

@router.get('/', response_model= List[ShowCustomersSchema])
def index(repository: CustomersRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id:int , customer: CustomersSchema, repository: CustomersRepository = Depends()):
    repository.update(id, customer.dict())

@router.get('/{id}', response_model= ShowCustomersSchema)
def show(id:int, repository: CustomersRepository = Depends()):
    return repository.get_by_id(id)