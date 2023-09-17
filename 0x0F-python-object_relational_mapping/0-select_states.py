#!/usr/bin/python3
import MySQLdb
from sys import argv


def get_database():
    """
    a function to get the database
    """
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        username=argv[1],
        pswd=argv[2],
        db=argv[3]
    )
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()
    

if __name__=="__main__":
    get_database()
    
    