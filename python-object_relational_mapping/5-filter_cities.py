#!/usr/bin/python3
"""
    task 5
    Write a script that takes in the name of a state as an argument
    and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""


def main():
    from MySQLdb import connect

    db = connect(host="localhost", port=3306, user=mysql_username,
                 passwd=mysql_password, db=database_name, charset="utf8")
    cursor_aux = db.cursor()
    cursor_aux.execute("SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = '{}' ORDER BY \
        cities.id ASC".format(state_name_searched))
    rows = cursor_aux.fetchall()
    cnt = 0
    for r in rows:
        if r[2] == state_name_searched:
            print(f"{r[1]}", end='')
        if cnt < len(rows) - 1:
            print(", ", end='')
        cnt += 1
    print()
    cursor_aux.close()
    db.close()


if __name__ == "__main__":
    from sys import argv

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]
    if ';' not in state_name_searched:
        main()
