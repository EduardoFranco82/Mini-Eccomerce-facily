from pydantic import BaseModel
from app.api.categorie.schemas import ShowCategorieSchema
from app.api.suppliers.schemas import ShowSuppliersSchema


class ProductSchema(BaseModel):
    description: str
    price: float
    technical_details: str
    image: str
    visible: bool
    categorie_id : int
    supplier_id : int


class ShowProductSchema(ProductSchema):
    id: int
    categorie: ShowCategorieSchema
    supplier : ShowSuppliersSchema
    
    class Config:
        orm_mode = True
