import datetime
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import DateTime
#from app.api.user.schemas import UserSchema
from datetime import date
from app.api.user.schemas import UserSchemas_customer
from app.models.models import User


class UserSchema(BaseModel):
    email: str
    password: str
    display_name: str
    
class CustomerSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: date
   # user_id: UserSchemas_customer
    user : UserSchema

class UpdateUserSchema(UserSchema):
    id:int

class UpdateCustomersSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    birth_date: date
   # user_id: UserSchema
    user : UpdateUserSchema
    


class ShowCustomersSchema(BaseModel):
    id: int
   # user: UserSchema

    class Config:
        orm_mode = True
