#!/usr/bin/python3
"""
    task 14
    write a script 14-model_city_fetch_by_state.py that prints
    all City objects from the database hbtn_0e_14_usa:
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
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

    for city in session.query(City).order_by(City.id).all():
        for state in session.query(State).order_by(State.id).all():
            if state.id == city.state_id:
                print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
