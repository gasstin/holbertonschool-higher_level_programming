#!/usr/bin/python3
"""
    task 15
    Write a python file that contains the class definition
    of a State and an instance Base = declarative_base().
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """creates a state

    Args:
        id, name, cities
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
