#!/usr/bin/python3
""" Module listing all states starting with N (upper N) from hbtn_0e_0_usa."""
import MySQLdb
import sys


def filter_states():
    """ Function listing all states starting with N (upper N)
        from hbtn_0e_0_usa.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute(
        'SELECT * FROM states WHERE name LIKE BINARY "N%" \
            ORDER BY states.id ASC')
    result = cur.fetchall()
    for row in result:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states()
