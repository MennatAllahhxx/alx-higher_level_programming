#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


def filter_database():
    """
    a function to get the database
    """

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT cities.name\
                   FROM cities \
                   INNER JOIN states\
                   ON cities.state_id = states.id\
                   WHERE states.name='{:s}' \
                   ORDER BY cities.id ASC\
                   ".format(argv[4]))
    rows = cursor.fetchall()
    result = []

    for row in rows:
        result.append(row[0])

    print(", ".join(result))
    cursor.close()
    db.close()


if __name__ == '__main__':
    filter_database()
