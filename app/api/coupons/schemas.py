from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import DateTime





class CouponsSchema(BaseModel):
    code: str
    expire_at : DateTime
    limit : int
    type :str
    value : float




class ShowCouponsSchema(CouponsSchema):
    id: int
       
    class Config:
        orm_mode = True

