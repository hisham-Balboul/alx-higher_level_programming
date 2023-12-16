#!/usr/bin/python3
"""Lists all cities by state"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, host='localhost',
                         user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
               FROM `cities` as `c` \
               INNER JOIN `states` as `s` \
               ON `c`.`state_id` = `s`.`id` \
               ORDER BY `c`.`id`")
    [print(city) for city in c.fetchall()]
