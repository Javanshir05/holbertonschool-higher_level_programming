#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
The script uses a JOIN to display the state name for each city.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    c = db.cursor()

    # Execute the JOIN query
    # We select city ID, city name, and state name by joining on state_id
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    c.execute(query)

    # Fetch and print results
    rows = c.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    c.close()
    db.close()
