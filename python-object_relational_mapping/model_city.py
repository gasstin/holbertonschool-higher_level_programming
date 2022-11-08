#!/usr/bin/python3
"""
    task 14
    WWrite a Python file similar to model_state.py 
    named model_city.py that contains the class definition of a City
"""


from sqlalchemy import Column, Integer, String
from model_state import Base

class City(Base):
    """creates a city

    Args:
        id, name, state_id
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeingKey('states.id'))
    