#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
This script is safe from MySQL injections.
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

    # Create a cursor object
    c = db.cursor()

    # Use a parameterized query to prevent SQL injection.
    # The %s is a placeholder, and the actual value is passed as a tuple.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    c.execute(query, (sys.argv[4],))

    # Fetch and print the results
    rows = c.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    c.close()
    db.close()
