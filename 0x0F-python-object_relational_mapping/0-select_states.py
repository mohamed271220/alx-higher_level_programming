#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>

This script connects to a MySQL server running on localhost at port 3306,
fetches all states from the states table in the specified database,
and prints the results sorted in ascending order by states.id.
"""


import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to fetch all states sorted by id
        query = "SELECT * FROM states ORDER BY id;"
        cursor.execute(query)
        # Fetch all rows from the result set
        results = cursor.fetchall()

        # Print each row as per the example format
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)
    finally:
        # Close cursor and database connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
