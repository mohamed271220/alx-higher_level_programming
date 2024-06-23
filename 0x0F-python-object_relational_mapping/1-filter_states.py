#!/usr/bin/python3
"""
Module to list all states from a database starting with 'N'
"""

import MySQLdb
import sys


def filter_states():
    """
    Lists all states in a database starting with 'N'
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC"
        )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
