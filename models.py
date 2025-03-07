# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     email = Column(String(100), unique=True, index=True)
#     age = Column(Integer, nullable=True)

#     # Relationship with orders
#     orders = relationship("Order", back_populates="user")

# class Restaurant(Base):
#     __tablename__ = "restaurants"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     location = Column(String(100))

#     # Relationship with orders
#     orders = relationship("Order", back_populates="restaurant")

# class Order(Base):
#     __tablename__ = "orders"

#     id = Column(Integer, primary_key=True, index=True)
#     description = Column(String(100))
#     user_id = Column(Integer, ForeignKey('users.id'))  # Foreign Key to User table
#     restaurant_id = Column(Integer, ForeignKey('restaurants.id'))  # Foreign Key to Restaurant table

#     # Relationships
#     user = relationship("User", back_populates="orders")
#     restaurant = relationship("Restaurant", back_populates="orders")




from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)