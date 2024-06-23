#!/usr/bin/python3
"""
Module to list all states from a database matching a user-provided name
"""

import MySQLdb
import sys


def filter_states():
    """
    Lists all states in a database matching a user-provided name
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}'"
    "ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
