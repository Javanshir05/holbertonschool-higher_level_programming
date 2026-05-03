#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
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

    # Query all State objects that contain the letter 'a'
    states_to_delete = session.query(State).filter(
        State.name.contains('a')
    ).all()

    # Iterate through the results and delete each object from the session
    for state in states_to_delete:
        session.delete(state)

    # Commit all changes to the database
    session.commit()

    # Close the session
    session.close()
