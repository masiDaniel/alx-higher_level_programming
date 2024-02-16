#!/usr/bin/python3
"""values in the table of hbtn_0e_0_usa where name matches argument keyed in """

import MySQLdb
import sys


def display_info():
    """Function listing all the states"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute(
        'SELECT * FROM states WHERE name LIKE BINARY "{}" \
            ORDER BY states.id ASC'.format(sys.argv[4])
    )
    result = cur.fetchall()

    for rows in result:
        print(rows)

    cur.close()
    db.close()


if __name__ == "__main__":
    display_info()
