from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from app.services.customer_service import CustomerService
from app.api.coupons.schemas import UpdateCuponsSchema
from .schemas import CustomerSchema, ShowCustomersSchema, UpdateCustomersSchema
from app.repositories.customers_repository import CustomersRepository
from app.models.models import Customers
from typing import List
from app.common.exceptions import Admin_userAlreadyExistsEmailException
router = APIRouter()


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(customer: CustomerSchema, service: CustomerService = Depends()):
    try:
     return   service.create_customer(customer)
    
    except Admin_userAlreadyExistsEmailException as msg:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail= msg.message)

@router.get('/', response_model= List[ShowCustomersSchema])
def index(repository: CustomersRepository = Depends()):
    return repository.get_all()

@router.put('/{id}')
def update(id:int , customer: UpdateCustomersSchema, service: CustomerService = Depends()):
  return  service.update_customer(customer,id)

@router.get('/{id}', response_model= ShowCustomersSchema)
def show(id:int, repository: CustomersRepository = Depends()):
    return repository.get_by_id(id)

