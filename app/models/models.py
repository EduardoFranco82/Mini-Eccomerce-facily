from ast import Str
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DATETIME, Boolean, Date, Float, Integer, String
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

class Coupons (Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True)
    code = Column (String(10))
    expire_at = Column (DATETIME)
    limit = Column (Integer)
    type = Column (String(15))
    value = Column (Float)

class Customers (Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    phone_number = Column(String(15))
    genre = Column(String(45))
    document_id = Column(String(45))
    birth_date = Column(Date)
    user_id = Column(Integer)

class Addresses (Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    address = Column(String(255))
    city = Column(String(45))
    state = Column(String(2))
    number = Column(String(10))
    zipcode = Column(String(6))
    neighbourhood = Column(String(45))
    primary = Column(Boolean, default= True)
    customer_id = Column(Integer)