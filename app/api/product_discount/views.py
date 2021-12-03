from fastapi import APIRouter
from .schemas import ShowProductDiscountSchema, ProductDiscountSchema
from fastapi.params import Depends
from typing import List
from fastapi import APIRouter, status
from app.repositories.product_discount_repository import PaymentDiscountRepository
from app.models.models import ProductDiscount


router = APIRouter()




@router.post('/', status_code=status.HTTP_201_CREATED)
def create(product_discount: ProductDiscountSchema, 
              repository: PaymentDiscountRepository = Depends()):
    repository.create(ProductDiscount(**product_discount.dict()))



@router.get('/', response_model = List[ShowProductDiscountSchema])
def index(repository: PaymentDiscountRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, product_discount: ProductDiscountSchema,
        repository: PaymentDiscountRepository = Depends()):
    repository.update(id, product_discount.dict())

@router.get('/{id}', response_model=ShowProductDiscountSchema)
def show(id: int, repository: PaymentDiscountRepository = Depends()):
    return repository.get_by_id(id)
