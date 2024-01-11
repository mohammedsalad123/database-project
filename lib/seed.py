from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker

# Step 1: Define the Model
Base = declarative_base()

class Vendor(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    product = Column(String)
    price = Column(Integer)

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    vendor_id = Column(Integer, ForeignKey('vendors.id'))

    # Define relationships
    customer = relationship('Customer', back_populates='admins')
    vendor = relationship('Vendor', back_populates='admins')

# Establish SQLite database connection
engine = create_engine('sqlite:///your_database.db', echo=True)

# Create tables
Base.metadata.create_all(engine)

# Step 2: Create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Step 3: Add Data to the Tables
fake = Faker()

# Seed data for vendors
vendors = [
    Vendor(
        name=fake.company(),
        product=fake.word(),
        price=fake.random_int(min=10, max=1000)
    ) for _ in range(5)
]
session.add_all(vendors)

# Seed data for customers
customers = [
    Customer(
        name=fake.name(),
        location=fake.city()
    ) for _ in range(2)
]
session.add_all(customers)

# Seed data for admins
admins = [
    Admin(
        name=fake.name(),
        customer_id=fake.random_int(min=1, max=2),  # Adjust max based on the number of customers
        vendor_id=fake.random_int(min=1, max=5)
    ) for _ in range(1)
]
session.add_all(admins)

# Commit changes to the database
session.commit()

# Step 4: Close the Session
session.close()
