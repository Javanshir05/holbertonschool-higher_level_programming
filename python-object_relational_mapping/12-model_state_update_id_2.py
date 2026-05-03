#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
Updates the State where id = 2 to "New Mexico".
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create engine and connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 1. Fetch the state object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # 2. If the state exists, update its name
    if state_to_update:
        state_to_update.name = "New Mexico"
        # 3. Commit the change to the database
        session.commit()

    # Close the session
    session.close()
