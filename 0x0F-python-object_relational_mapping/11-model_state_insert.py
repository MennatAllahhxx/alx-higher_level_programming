#!/usr/bin/python3
"""
a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    lou = State(name="Louisiana")

    session.add(lou)
    session.commit()
    print(lou.id)
    session.close()


if __name__ == '__main__':
    my_filter_database()
