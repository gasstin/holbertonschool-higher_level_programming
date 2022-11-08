#!/usr/bin/python3
"""
    task 10
    Write a script that prints the State object
    with the name passed as argument from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]
    if ';' in state_name_searched:
        exit()

    engine = create_engine(f'mysql+mysqldb://\
{mysql_username}:{mysql_password}@localhost:3306/{database_name}',
                           pool_pre_ping=True,)
    Base.metadata.create_all(engine)  # Create an engine

    session = Session(engine)  # Create a session

    found = 0
    for state in session.query(State).order_by(State.id)\
            .filter_by(name=state_name_searched):
        if state:
            print(f"{state.id}")
            found = 1
    if not found:
        print("Not found")
    session.close()
