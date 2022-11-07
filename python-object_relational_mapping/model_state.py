#!/usr/bin/pyhton3
"""
    task 6
    Write a python file that contains the class definition of a State and an instance Base = declarative_base():    
"""

from
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """creates a state

    Args:
        Base (_type_): _description_
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, autoincrement=True, primary_key= True)
    name = Column(String(128), nulleable=False)