from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    display_name: str
    email: str
    password: str
    role : str #Optional[str]  ='customer'

class UserSchemas_customer(BaseModel):
    display_name: str
    email: str
    password: str
    role : str #Optional[str]  ='customer'