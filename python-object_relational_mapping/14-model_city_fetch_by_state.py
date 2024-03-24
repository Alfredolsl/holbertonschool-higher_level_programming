#!/usr/bin/python3
"""prints all City objects from db hbtn_0e_14_usa"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    URL = "mysql+mysqldb://{}:{}\
           @localhost:3306/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(URL)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    instances = session.query(State.name, City.id, City.name)\
        .filter(State.id == City.state_id)

    for instance in instances:
        print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))
