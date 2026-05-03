#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to a MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to execute queries
    c = db.cursor()

    # Use LIKE BINARY to ensure the 'N' is uppercase
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    c.execute(query)

    # Fetch and print the results
    rows = c.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    c.close()
    db.close()
