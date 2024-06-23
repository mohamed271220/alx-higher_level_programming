#!/usr/bin/python3
"""
Defines the State class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


Class State(Base):
    """
    Defines the states table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True, autoincrement=True)
    name = Column(String(128), nullable=False)
