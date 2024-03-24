#!/usr/bin/python3
"""changes the name of a State object from db hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    URL = "mysql+mysqldb://{}:{}\
           @localhost:3306/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(URL)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    updateState = session.query(State).filter_by(id=2).first()
    updateState.name = "New Mexico"

    session.commit()
