#!/usr/bin/python3
"""
    task 6
    Write a python file that contains the class definition
    of a State and an instance Base = declarative_base().
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    
    engine = create_engine(f'mysql+mysqldb://\
            {mysql_username}:{mysql_password}@localhost:3306/{database_name}', pool_pre_ping=True)
    Base.metadata.create_all(engine) # Create an engine
    
    Session = sessionmaker(bind=engine) # Create a class session
    
    session = Session(engine) # Create a session
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()




