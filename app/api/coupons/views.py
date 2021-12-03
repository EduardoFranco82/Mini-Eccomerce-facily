from typing import List
from fastapi import APIRouter, status
from fastapi.applications import FastAPI
from fastapi.params import Depends
from app.models.models import Coupons
from app.repositories.coupons_repository import CouponsRepository
from .schemas import CouponsSchema, ShowCouponsSchema

router = FastAPI()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(coupon: CouponsSchema, repository: CouponsRepository = Depends()):
    repository.create(Coupons(**coupon.dict()))


@router.get('/', response_model=List[ShowCouponsSchema])
def index(repository: CouponsRepository = Depends()):
    return repository.get_all


@router.put('/{id}')
def update(id: int, coupon:CouponsSchema, repository:CouponsRepository = Depends()):
    repository.update(id, coupon.dict())

@router.get('/{id}', response_model=ShowCouponsSchema)
def show(id: int, repository: CouponsRepository = Depends()):
    return repository.get_by_id(id)