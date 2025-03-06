#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish MySQL connection using command line arguments
    db = MySQLdb.connect(
        host="localhost",    # Connect to localhost
        port=3306,           # Default MySQL port
        user=sys.argv[1],    # MySQL username (1st argument)
        passwd=sys.argv[2],  # MySQL password (2nd argument)
        db=sys.argv[3]       # Database name (3rd argument)
    )

    # Create cursor to execute SQL queries
    cur = db.cursor()

    # Execute query to select all states ordered by ID
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results and display them
    for row in cur.fetchall():
        print(row)

    # Clean up: close cursor and database connection
    cur.close()
    db.close()
