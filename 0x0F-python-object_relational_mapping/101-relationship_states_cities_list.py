#!/usr/bin/python3
"""
This script lists all `State` objects, and corresponding `City` objects, contained in the
database `hbtn_0e_101_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State

if __name__ == "__main__":
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    
    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()
    
    # Query the database for all `State` objects
    for state in session.query(State).order_by(State.id):
        # Print the `State` id and the `State` name
        print("{}: {}".format(state.id, state.name))
        
        # For each `City` object in the `cities` attribute of the `State` object
        for city in state.cities:
            # Print the `City` id and the `City` name
            print("\t{}: {}".format(city.id, city.name))
