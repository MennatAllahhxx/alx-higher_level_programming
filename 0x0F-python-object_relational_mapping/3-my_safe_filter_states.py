#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections
"""
import MySQLdb
from sys import argv


def my_safe_filter_database():
    """
    a function to filter the database
    """

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s \
        ORDER BY id ASC", (argv[4],))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    my_safe_filter_database()
