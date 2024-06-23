#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>

This script connects to a MySQL server running on localhost at port 3306,
fetches all states from the states table in the specified database, and
prints the results sorted in ascending order by states.id.
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

    # Connect to MySQL database
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)
    
    # Create a MySQL cursor
    cursor = db.cursor()
    
    # Execute the SQL query
    query = "SELECT * FROM states ORDER BY id;"
    try:
        cusrsor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        db.close()
        sys.exit(1)

    # Close cursor and database connection
    cursor.close()
    db.close()
