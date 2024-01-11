from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
engine  = create_engine('sqlite:///sales.db') #creates the engine sales

class Vendor(Base):
    __tablename__ = 'vendors'

    id = Column (Integer(),primary_key=True)
    name = Column(String())
    product = Column(Integer())
    price = Column(Integer())

# connection to admin
    admin = relationship('Admin',backref='vendor')

    def __repr__(self):
        return f"vendor{self.id}."\
        f"  {self.name}"\
        f"Product:  {self.product}"\
        f"Price: {self.price}"
        
class Buyer(Base):
    __tablename__ = 'buyers'

    id  = Column(Integer(),primary_key=True)
    name = Column(String())
    location = Column(String())
# connection to admin
   
    admin = relationship('Admin',backref='buyer')

# represent data 
    def __repr__(self):
        return f"{self.id},  buyer Name:  {self.name}."
    
class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer(),primary_key=True)
    name = Column(String())

# establish connection to both vendor and customer 
    customer_id = Column(Integer(), ForeignKey ('buyers.id'))
    vendor_id = Column(Integer(), ForeignKey('vendors.id'))
    
    def __repr__ (self):
        return f"Admin Name: {self.name}."

# Base.metadata.create_all(engine)
    
        

    