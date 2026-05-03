#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Setup the connection to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the new State object
    new_state = State(name="Louisiana")

    # Add the object to the session
    session.add(new_state)

    # Commit the session to the database
    session.commit()

    # Print the new id
    # SQLAlchemy refreshes the object with the new ID after commit
    print("{}".format(new_state.id))

    # Close the session
    session.close()
