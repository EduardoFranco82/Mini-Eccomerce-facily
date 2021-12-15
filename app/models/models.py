from ast import Str
from sqlalchemy import Column
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import  Boolean, Date, DateTime, Float, Integer, String
from app.db.db import Base




class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement= True)
    name = Column(String(45))


class Categorie(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement= True)
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
    #discounts = relationship('ProductDiscount')#foi incluido por paginaçao no catalogo

class ProductDiscount(Base):
    __tablename__ = 'product_discount'
    id = Column(Integer, primary_key=True)
    mode = Column (String(45))
    value = Column(Float)
    payment_method_id = Column(Integer, ForeignKey('payment_methods.id'))
    payment_method = relationship(PaymentMethod)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship(Product , backref = 'discounts')# atençao estudar

class Coupons (Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True)
    code = Column (String(10), unique= True)
    expire_at = Column (DateTime)
    limit = Column (Integer)
    type = Column (String(15))
    value = Column (Float)




class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    display_name = Column(String(100))
    email = Column(String(50))
    role = Column(String(10))
    password = Column(String(100))




class Customers (Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(45))
    last_name = Column(String(45))
    phone_number = Column(String(15))
    genre = Column(String(45))
    document_id = Column(String(45), unique=True)
    birth_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

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
    customer_id = Column(Integer, ForeignKey ('customers.id'))
    customer = relationship(Customers)
    
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    number = Column(String(10))
    status = Column(String(15))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship(Customers)
    created_at = Column(DateTime)
    address_id = Column(Integer, ForeignKey('addresses.id'))
    total_value = Column(Float(10,2))
    payment_form_id = Column(Integer)
    total_discount = Column(Float(10,2))

class OrderStatus(Base):
    __tablename__ = 'order_statuses'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship(Order)
    status = Column(String(15))
    created_at = Column(DateTime)

class OrderProducts(Base):
    __tablename__ = 'order_products'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship(Order)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship(Product)
    quantity = Column(Integer)