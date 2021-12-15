from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from .schemas import ShowProductDiscountSchema, ProductDiscountSchema
from fastapi.param_functions import Depends
from typing import List
from fastapi import APIRouter, status
from app.repositories.product_discount_repository import ProductDiscountRepository
from app.models.models import ProductDiscount
from app.services.product_discount_service import ProductDiscountService
from app.common.exceptions import PaymentMethodDiscountAlreadyExistsException, PaymentMethodsNotAvailableException

from app.services.auth_service import get_user, only_admin

router = APIRouter(dependencies=[Depends(only_admin)])




@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product_discount: ProductDiscountSchema, 
              service: ProductDiscountService = Depends()):
    try:
        service.create_discount(product_discount)
    except PaymentMethodDiscountAlreadyExistsException as payment_method:
        raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST, detail= payment_method.message)
    except PaymentMethodsNotAvailableException as payment_method_not_available:
        raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST, detail= payment_method_not_available.message)

@router.get('/', response_model = List[ShowProductDiscountSchema])
def index(repository: ProductDiscountRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, product_discount: ProductDiscountSchema,
        repository: ProductDiscountRepository = Depends()):
    repository.update(id, product_discount.dict())

@router.get('/{id}', response_model=ShowProductDiscountSchema)
def show(id: int, repository: ProductDiscountRepository = Depends()):
    return repository.get_by_id(id)

@router.delete('/{id}')
def delete(id:int, repository: ProductDiscountRepository = Depends()):
    return repository.remove(id)