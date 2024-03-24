#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

if __name__ == "__main__":
    URL = "mysql+mysqldb://{}:{}\
           @localhost:3306/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(URL)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        instance = session.query(State).first()
        print(instance.id, instance.name, sep=": ")
    except NoResultFound:
        print("Nothing")
