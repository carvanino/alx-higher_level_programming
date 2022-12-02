#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
list all the cities of that state
"""

import MySQLdb
import sys

arg = sys.argv[4]

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db='hbtn_0e_4_usa')
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
            JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC;", (arg, ))
    cities = cur.fetchall()

    for i, city in enumerate(cities):
        if i == len(cities) - 1:
            print(city[0])
        else:
            print(city[0], end=', ')
    cur.close()
    db.close()
