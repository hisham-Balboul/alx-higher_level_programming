#!/usr/bin/python3
""" Displays all cities of a state from the states table """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, host='localhost',
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities INNER JOIN states ON \
               cities.state_id=states.id WHERE states.name LIKE %s \
               ORDER BY cities.id ASC", [argv[4]])
    rows = c.fetchall()
    print(", ".join(row[0] for row in rows))
