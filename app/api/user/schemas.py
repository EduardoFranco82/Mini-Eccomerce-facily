from pydantic import BaseModel


class UserSchema(BaseModel):
    display_name: str
    email: str
    password: str
    role = 'customer'

class UserSchemas_customer(BaseModel):
    display_name: str
    email: str
    password: str
    role ='customer'