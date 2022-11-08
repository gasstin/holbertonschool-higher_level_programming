#!/usr/bin/python3
"""
    task 13
    Write a script that deletes all State objects with
    a name containing the letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    engine = create_engine(f'mysql+mysqldb://\
{mysql_username}:{mysql_password}@localhost:3306/{database_name}',
                           pool_pre_ping=True,)
    Base.metadata.create_all(engine)  # Create an engine

    session = Session(engine)  # Create a session

    for state in session.query(State).all():
        if 'a' in state.name:
            session.delete(state)
            session.commit()

    session.close()
