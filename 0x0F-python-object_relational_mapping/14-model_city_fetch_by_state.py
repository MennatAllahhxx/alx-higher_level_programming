#!/usr/bin/python3
"""
a script 14-model_city_fetch_by_state.py that prints all
City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
from sys import argv


def get_database():
    """
    a function to get the database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()
    rows = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id)

    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == '__main__':
    get_database()
