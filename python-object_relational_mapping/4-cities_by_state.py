#!/usr/bin/python3
"""
    task 4
    Write a script that lists all cities from the database hbtn_0e_4_usa
"""


def main():
    from MySQLdb import connect

    db = connect(host="localhost", port=3306, user=mysql_username,
                 passwd=mysql_password, db=database_name, charset="utf8")
    cursor_aux = db.cursor()
    cursor_aux.execute("SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    rows = cursor_aux.fetchall()
    for r in rows:
        print(r)
    cursor_aux.close()
    db.close()


if __name__ == "__main__":
    from sys import argv

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    main()
