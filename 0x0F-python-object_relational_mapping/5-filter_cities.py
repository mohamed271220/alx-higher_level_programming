#!/usr/bin/python3
"""
Module to list all cities from a specific state in a database
"""

import MySQLdb
import sys


def filter_cities():
    """
    Lists all cities from a specific state in a database
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = ("SELECT cities.name "
             "FROM cities "
             "INNER JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    print(", ".join(city[0] for city in rows))
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities()
