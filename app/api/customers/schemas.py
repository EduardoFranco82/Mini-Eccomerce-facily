import datetime
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import DateTime
#from app.api.users.schemas import ShowUsersSchema


class CustomersSchema(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    genre: str
    document_id: str
    birth_date: datetime.date
    user_id: int


class ShowCustomersSchema(CustomersSchema):
    id: int
    #user: ShowUsersSchema

    class Config:
        orm_mode = True
