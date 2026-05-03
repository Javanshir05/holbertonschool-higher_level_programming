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
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    c = db.cursor()
    
    c.execute("SELECT * FROM states ORDER BY id ASC")
    
    rows = c.fetchall()
    for row in rows:
        print(row)
    
    c.close()
    db.close()
