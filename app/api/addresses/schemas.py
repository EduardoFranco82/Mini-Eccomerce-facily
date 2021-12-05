from pydantic import BaseModel
from app.api.customers.schemas import ShowCustomersSchema

class AdressesSchema(BaseModel):
    address: str
    city: str
    state: str
    number: str
    zipcode: str
    neighbourhood: str
    primary: bool
    coustomer_id: int

class ShowAdressesSchema(AdressesSchema):
    id: int
    coustomer: ShowCustomersSchema

    class Config:
        orm_mode = True