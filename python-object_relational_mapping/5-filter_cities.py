#!/usr/bin/python3
"""
Lists all cities of a state provided as an argument.
The script is safe from SQL injection and uses a single execute() call.
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

    # Join cities and states to filter by the state name provided in sys.argv[4]
    # Parameterized query (%s) prevents SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    c.execute(query, (sys.argv[4],))

    # Fetch all results
    rows = c.fetchall()

    # Format the output: Extract names from tuples and join with commas
    cities_list = [row[0] for row in rows]
    print(", ".join(cities_list))

    # Close cursor and connection
    c.close()
    db.close()
