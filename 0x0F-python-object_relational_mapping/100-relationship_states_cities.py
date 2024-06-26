#!/usr/bin/python3
"""
This script creates the `State` "California" with the `City` "San Francisco" in the database
`hbtn_0e_100_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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
    
    # Create a new `State` object with the name "California"
    california = State(name="California")
    
    # Assign a list of `City` objects to the `cities` attribute of the `State` object
    california.cities = [City(name="San Francisco")]
    
    # Add the new `State` object to the session
    session.add(california)
    
    # Commit the session to write the changes to the database
    session.commit()
