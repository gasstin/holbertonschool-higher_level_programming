#!/usr/bin/python3
"""
    task 2
    Write a script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
"""


def main():
    from MySQLdb import connect

    db = connect(host="localhost", port=3306, user=mysql_username,
                 passwd=mysql_password, db=database_name, charset="utf8")
    cursor_aux = db.cursor()
    cursor_aux.execute(f"SELECT * FROM states WHERE name = '{state_name_searched}' ORDER BY id ASC")
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
    state_name_searched = argv[4]
    main()
