from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Float, Integer, String
from app.db.db import Base




class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))


class Categorie(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))


class PaymentMethod(Base):
    __tablename__ = 'payment_methods'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    enabled = Column(Boolean, default=True)



class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(Float(10, 2)) # --> 10 quantidades, 2 casas decimais
    technical_details = Column(String(255))
    image = Column(String(255))
    visible = Column(Boolean, default=True)
    categorie_id = Column(Integer, ForeignKey('categories.id'))
    categorie = relationship(Categorie)
    supplier_id = Column (Integer, ForeignKey('suppliers.id'))
    supplier = relationship(Supplier)

class ProductDiscount(Base):
    __tablename__ = 'product_discount'

    id = Column(Integer, primary_key=True)
    mode = Column (String(45))
    value = Column(Float)
    payment_method_id = Column(Integer, ForeignKey('payment_methods.id'))
    payment_method = relationship(PaymentMethod)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship(Product)