#!/usr/bin/python3
"""
This script prints the first `State` object from the database `hbtn_0e_6_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()
    
    # Query the database for the first `State` object
    state = session.query(State).order_by(State.id).first()
    
    # If no `State` object is found, print "Nothing"
    if state is None:
        print("Nothing")
    else:
        # Otherwise, print the `id` and `name` of the `State` object
        print("{}: {}".format(state.id, state.name))
