#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv


def delete_database():
    """
    a function to delete the database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()
    rows = session.query(State).filter(State.name.like('%a%')).all()

    for row in rows:
        session.delete(row)

    session.commit()
    session.close()


if __name__ == '__main__':
    delete_database()
