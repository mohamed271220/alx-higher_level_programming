#!/usr/bin/python3
"""
This script lists all `City` objects from the database `hbtn_0e_101_usa`.
For each `City` object, it prints the `City` id, the `City` name, and the `State` name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City

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
    
    # Query the database for all `City` objects
    for city in session.query(City).order_by(City.id):
        # Print the `City` id, the `City` name, and the `State` name
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
