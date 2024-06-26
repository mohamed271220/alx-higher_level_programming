#!/usr/bin/python3
"""
This script deletes a `State` object with the name "California" from the database `hbtn_0e_100_usa`.
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
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()
    
    # Query the database for the `State` object with the name "California"
    california = session.query(State).filter(State.name == "California").first()
    
    # If the `State` object exists
    if california is not None:
        # Delete the `State` object
        session.delete(california)
        
        # Commit the session to write the changes to the database
        session.commit()
