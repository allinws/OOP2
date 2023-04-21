from random import choice
import os
import sys
from pathlib import Path

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Table, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

if os.path.exists('ecommerce.db'):
    os.remove('ecommerce.db')

current_path = Path(sys.argv[0] if __name__ == "__main__" else __file__).resolve().parent

# Skapa engine och session
db_path = current_path / "ecommerce.db"
if db_path.exists():
    os.remove(db_path)
engine = create_engine(f'sqlite:///{db_path}', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

# Skapa basen för modeller
Base = declarative_base()


""" MODELLER """

class OrderItem(Base):
    __tablename__ = 'order_items'
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    orders = relationship('Order', secondary='order_items')

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    products = relationship('Product', secondary='order_items')
    customer = relationship('Customer', back_populates='orders')

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    orders = relationship('Order', back_populates='customer')

Base.metadata.create_all(engine)



""" TESTDATA """

products = [
    Product(name=f'Product {i+1}', price=(i+1) * 10) for i in range(10)
]

customers = [
    Customer(name=f'Customer {i+1}') for i in range(10)
]

orders = []
for _ in range(300):
    order = Order(customer=choice(customers))
    num_products = choice([1, 2, 3, 4])
    order_products = set()
    while len(order_products) < num_products:
        order_products.add(choice(products))
    for product in order_products:
        order.products.append(product)
    orders.append(order)

session.add_all(products + customers + orders)
session.commit()



# """ QUERIES """

# 1. Lista alla kunder
customers = session.query(Customer).all()
for customer in customers:
    print(customer.name)

# 2. Visa alla ordrar för en specifik kund
print('Orders for customer 1: \n')
customer_orders = session.query(Order).filter(Order.customer_id == 1).all()
for order in customer_orders:
    print(f"Order ID: {order.id}, Customer ID: {order.customer_id}")
print('\n')

# 3. Visa alla produkter i en specifik order
print('Products in order 1: \n')
order_products = session.query(Product).filter(Product.orders.any(id=1)).all()
for product in order_products:
    print(f"Product ID: {product.id}, Product Name: {product.name}")
print('\n')

# 4. Lista alla produkter sorterade efter pris
print('Products sorted by price: \n')
sorted_products = session.query(Product).order_by(Product.price).all()
for product in sorted_products:
    print(f"Product ID: {product.id}, Product Name: {product.name}, Price: {product.price}")
print('\n')

# 5. Lista antalet ordrar per kund
print('Order count by customer: \n')
order_count_by_customer = (
    session.query(Customer.name, Customer.id, func.count(Order.id).label("order_count"))
    .join(Order, Order.customer_id == Customer.id)
    .group_by(Customer.id)
    .all()
)
for item in order_count_by_customer:
    print(f"Customer ID: {item.id}, Customer Name: {item.name}, Order Count: {item.order_count}")
print('\n')

# Ändra en produkt
print('Change a product: \n')
product_to_update = session.query(Product).filter(Product.id == 1).one()
print('Product pre change:', product_to_update.name, product_to_update.price)
product_to_update.price = 100  # Ändra priset på produkten
session.commit()
product_after_change = session.query(Product).filter(Product.name == product_to_update.name).one()
print('Product post change:', product_after_change.name, product_after_change.price)
print('\n')