from typing import List
from fastapi import APIRouter, status, HTTPException
from fastapi.applications import FastAPI
from fastapi.param_functions import Depends
from app.common.exceptions import CouponCodeAlreadyExistsException
from app.models.models import Coupons
from app.repositories.coupons_repository import CouponsRepository
from .schemas import CouponsSchema, ShowCouponsSchema, UpdateCuponsSchema
from app.services.create_coupons_service import CreateCouponsService

from app.services.auth_service import get_user, only_admin

router = APIRouter(dependencies=[Depends(only_admin)])

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(coupon: CouponsSchema, service: CreateCouponsService = Depends()):
    try: 
      return  service.unique_coupon(coupon)
        
    except CouponCodeAlreadyExistsException as exists_coupon:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= exists_coupon.message)


@router.get('/', response_model=List[ShowCouponsSchema])
def index(repository: CouponsRepository = Depends()):
    return repository.get_all


@router.put('/{id}')
def update(id: int, coupon:UpdateCuponsSchema, repository:CouponsRepository = Depends()):
  return  repository.update(id, coupon.dict())

@router.get('/{id}', response_model=ShowCouponsSchema)
def show(id: int, repository: CouponsRepository = Depends()):
    return repository.get_by_id(id)

@router.delete('/{id}')
def delete(id: int, repository:CouponsRepository = Depends()):
    repository.remove(id)