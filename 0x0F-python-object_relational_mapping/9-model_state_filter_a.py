#!/usr/bin/python3
"""
List all the State object that contains the letter 'a' from the database
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).where(
            State.name.like('%a%')).order_by(State.id)
    # states = session.query(State.name.like('%a%'))
    for state in states:
        print('{}: {}' .format(state.id, state.name))
