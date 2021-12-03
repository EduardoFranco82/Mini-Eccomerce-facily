from typing import List
from fastapi import APIRouter, status
from fastapi.params import Depends
from app.models.models import Supplier
from .schemas import ShowSuppliersSchema, SuppliersSchema
from app.db.db import get_db
from sqlalchemy.orm import Session
from app.repositories.supplier_repository import SupplierRepository


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(supplier: SuppliersSchema, repository: SupplierRepository = Depends()):
    repository.create(Supplier(**supplier.dict()))


@router.get('/', response_model=List[ShowSuppliersSchema])
def index(repository: SupplierRepository = Depends()):
    return repository.get_all()


@router.put('/{id}')
def update(id: int, supplier: SuppliersSchema, repository : SupplierRepository = Depends()):
    repository.update(id, supplier.dict())


@router.get('/{id}', response_model=ShowSuppliersSchema)
def show(id: int, repository : SupplierRepository = Depends()):
    return repository.get_by_id(id)