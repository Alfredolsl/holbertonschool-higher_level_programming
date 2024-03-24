#!/usr/bin/python3
"""Contains the class definition of a State and an instance Base."""
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

mymetadata = MetaData()
# Metadata parameter collects table objects. E.g., to issue CREATE statements.
Base = declarative_base(metadata=mymetadata)


class City(Base):
    """
    Class with id and name attributes for each city
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
