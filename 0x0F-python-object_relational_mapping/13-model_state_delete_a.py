#!/usr/bin/python3
"""
This script deletes all `State` objects with a name containing the letter 'a'
from the database `hbtn_0e_6_usa`.
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
    
    # Query the database for `State` objects with a name containing the letter 'a'
    # and delete them
    session.query(State).filter(
        State.name.like('%a%')).delete(synchronize_session='fetch')
    
    # Commit the session to write the changes to the database
    session.commit()
