#!/usr/bin/python3
"""
    task 17
    Write a script that lists all City objects
    from the database hbtn_0e_101_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
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

    for state in session.query(State).order_by(State.id).all():
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")
    session.close()
