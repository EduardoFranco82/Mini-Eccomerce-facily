import datetime
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import DateTime
from app.api.user.schemas import UserSchema
from datetime import date
from app.api.user.schemas import UserSchemas_customer

class CustomerSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: date
    user_id: UserSchemas_customer

class UpdateCustomersSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    birth_date: date
    user_id: int


class ShowCustomersSchema(CustomerSchema):
    id: int
    user: UserSchema

    class Config:
        orm_mode = True
