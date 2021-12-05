from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from app.models.models import Addresses
from .schemas import AdressesSchema, ShowAdressesSchema
from app.repositories.addresses_repository import AddressesRepository


router = APIRouter()

@router.post('/', status_code= status.HTTP_201_CREATED)
def create(address: AdressesSchema, repository: AddressesRepository = Depends()):
    repository.create(Addresses(**address.dict()))


@router.get('/', response_model=List[ShowAdressesSchema])
def index(repository:AddressesRepository = Depends ()):
    return repository.get_all()

@router.put('/{id}')
def update(id:int, address: AdressesSchema, repository: AddressesRepository = Depends ()):
    repository.update(id, address.dict())

@router.get('/{id}', response_model= ShowAdressesSchema)
def show(id:int, repository: AddressesRepository = Depends()):
    return repository.get_by_id(id)