#!/usr/bin/python3
"""a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""

#import MySQLdb
import MySQL.connector
import sys


if __name__ == "__main__":

    conn = MySQL.connector(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
                WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
