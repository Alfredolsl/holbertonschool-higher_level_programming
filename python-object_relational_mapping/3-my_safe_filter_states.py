#!/usr/bin/python3
"""takes args and shows matching values in states safe from MySQL injections"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    arg = argv[4]

    # We use a tuple, which is immutable (cannot be modified after creation)
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s", (arg, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
