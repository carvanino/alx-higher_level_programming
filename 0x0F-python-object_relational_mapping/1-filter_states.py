#!/usr/bin/python3
"""
List all states with name starting with 'N'
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db='hbtn_0e_0_usa')
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
            WHERE upper(states.name) LIKE 'N%'\
            ORDER BY states.id ASC")
    
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()

