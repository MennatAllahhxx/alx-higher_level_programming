#!/usr/bin/python3
"""
a script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv


def my_filter_database():
    """
    a function to filter the database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()
    row = session.query(State).filter(State.name == argv[4]).first()

    if row:
        print(row.id)
    else:
        print("Not found")

    session.close()


if __name__ == '__main__':
    my_filter_database()
