#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Connects to the database and fetches all states.
    """
    # Connect to a MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    # Create a cursor object
    c = db.cursor()
    # Execute the SQL query
    c.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all the rows
    rows = c.fetchall()
    for row in rows:
        print(row)
    # Close cursor and database connection
    c.close()
    db.close()
