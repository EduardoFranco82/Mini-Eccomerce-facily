from app.models.models import Addresses
from app.repositories.addresses_repository import AddressesRepository
from fastapi import Depends
from app.api.addresses.schemas import AdressesSchema
from app.common.exceptions import PrimaryAddressAlreadyExistsException



class AddressService:
    def __init__(self, address_repository : AddressesRepository = Depends()):
        self.address_repository = address_repository



    def switch_to_false_address(self, address):
        old_address = self.address_repository.is_primary(
            address.customer_id, address.primary
        )
        if address.primary and old_address:
            self.address_repository.update(old_address.id, {"primary": False})

    def create_address(self, address: AdressesSchema):
        self.switch_to_false_address(address)
        self.address_repository.create(Addresses(**address.dict()))
        
    def update_addres(self, id, address: AdressesSchema):
        self.switch_to_false_address(address)
        self.address_repository.update(id, address.dict())