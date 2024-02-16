#!/usr/bin/env python

from sys import argv
import MySQLdb


def cities_from_state():
    """
    lists cities from a state
    """
    db = MySQLdb.connect(host=argv[2], passwd=argv[3], db=argv[4])
    sql = "SELECT * FROM states WHERE name = {} ORDER BY id ASC;"
    sql.format(argv[4])
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for x in results:
        print(x)


if __name__ == "__main__":
    cities_from_state()
