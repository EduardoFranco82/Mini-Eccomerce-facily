from typing import List
from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from app.models.models import PaymentMethod, Product
from .schemas import PaymentMethodsSchema, ShowPaymentMethodsSchema
from fastapi.param_functions import Depends
from app.repositories.payment_method_repository import PaymentMethodRepository


from app.services.auth_service import get_user, only_admin

router = APIRouter(dependencies=[Depends(only_admin)])


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(payment_method: PaymentMethodsSchema, 
          repository: PaymentMethodRepository = Depends()):
   return repository.create(PaymentMethod(**payment_method.dict()))


@router.get('/', response_model=List[ShowPaymentMethodsSchema])
def index(repository: PaymentMethodRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, payment_method: PaymentMethodsSchema, 
           repository: PaymentMethodRepository = Depends()):
  return  repository.update(id, payment_method.dict())


@router.get('/{id}', response_model=ShowPaymentMethodsSchema)
def show(id: int, repository: PaymentMethodRepository = Depends()):
    return repository.get_by_id(id)
