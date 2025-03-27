from sqlalchemy import Column, String, Integer, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    items = relationship("Item", back_populates="category")

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True, nullable=False)
    description = Column(String, index=True)
    category_id =Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="items")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    