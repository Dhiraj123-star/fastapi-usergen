from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"    

    id = Column(Integer, primary_key=True, index=True)  # Added primary key
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    address = Column(String)
    phone = Column(String)
