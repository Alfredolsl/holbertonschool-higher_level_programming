#!/usr/bin/python3
"""takes name of the state as an arg and lists all cities of that state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    statename = argv[4]
    cur.execute("SELECT cities.name\
                 FROM cities\
                 INNER JOIN states ON states.id = cities.state_id\
                 WHERE states.name = %s", (statename, ))
    rows = cur.fetchall()
    rows_list = list(row[0] for row in rows)
    # Prints every item from rows_list with separator ', '
    print(*rows_list, sep=", ")
    cur.close()
    db.close()
