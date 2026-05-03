#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create the engine to connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class and instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object based on the name provided in sys.argv[4]
    # SQLAlchemy handles the escaping of sys.argv[4] to prevent SQL injection
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Display the id if found, otherwise "Not found"
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    # Close the session
    session.close()
