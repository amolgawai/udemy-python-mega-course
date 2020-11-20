""" simple sqlite exercise
    Note - This would be a great use case for database class,
    the implementation here is only for reference
"""

import sqlite3 as slt


def create_db(db_name, tbl_name):
    """ Create a sqlite3 database if doesn't exist

    Parameters
    ----------
    db_name : name of the database
    tbl_name: name of the table

    Returns
    -------
    conn : The database connection

    """
    conn = slt.connect(db_name)
    cur = conn.cursor()
    str_pre = "CREATE TABLE IF NOT EXISTS "
    str_cells = "(item TEXT, quantity INTEGER, price REAL)"
    str_db = str_pre + " " + tbl_name + " " + str_cells
    cur.execute(str_db)
    conn.commit()
    return conn


def insert_row(db_con, tbl_name, item, quantity, price):
    """ Insert row in database

    Parameters
    ----------
    tbl_name : table name

    db_con : database connection

    item : the name

    quantity : how much

    price : the price


    Returns
    -------
    nothing

    """
    cur = db_con.cursor()
    str_row_pre = "INSERT INTO "
    str_row_post = " VALUES(?,?,?)"
    str_row = str_row_pre + tbl_name + str_row_post
    cur.execute(str_row, (item, quantity, price))
    db_con.commit()


def get_db_rows(db_con, tbl_name):
    """ Get the database table rows

    Parameters
    ----------
    db_con : database connection

    tbl_name : table name


    Returns
    -------
    rows : table rows

    """
    cur = db_con.cursor()
    cur.execute("SELECT * FROM " + tbl_name)
    rows = cur.fetchall()
    return rows


def main():
    """ The main function """
    dbs_name = "lite.db"
    table_name = "store"
    db_conn = create_db(dbs_name, table_name)
    insert_row(db_conn, table_name, "Wine Glass", 8, 10.5)
    insert_row(db_conn, table_name, "Coffee Cup", 10, 5.0)
    print(get_db_rows(db_conn, table_name))
    db_conn.close()


if __name__ == '__main__':
    main()
