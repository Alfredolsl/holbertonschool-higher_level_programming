#!/usr/bin/python3
"""Contains the class definition of a State and an instance Base."""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
# Metadata parameter collects table objects. E.g., to issue CREATE statements.
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """
    Class with id and name attributes for each state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
