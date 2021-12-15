from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class CouponsType(str, Enum):
    VALUE = 'value'
    PERCENTAGE = 'percentage'


class CouponsSchema(BaseModel):
    code: str
    expire_at : datetime
    limit : int
    type : CouponsType
    value : float


class UpdateCuponsSchema(BaseModel):
    limit: int
    expire_at: datetime


class ShowCouponsSchema(CouponsSchema):
    id: int
       
    class Config:
        orm_mode = True

