#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument provided.
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

    # Create the query using format to insert the 4th argument (state name)
    # Binary is used to ensure case-sensitive matching
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
             ORDER BY id ASC".format(sys.argv[4])
    
    c.execute(query)

    # Fetch and print the results
    rows = c.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    c.close()
    db.close()
