#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv


def first_state():
    """
    a function to get the database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()
    row = session.query(State).order_by(State.id).first()

    if row:
        print('{}: {}'.format(row.id, row.name))
    else:
        print("Nothing")

    session.close()


if __name__ == '__main__':
    first_state()
