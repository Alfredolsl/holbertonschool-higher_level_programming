#!/usr/bin/python3
""" Displays all values in states of hbnt_0e_0_usa where name matches arg """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    arg = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(arg))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
