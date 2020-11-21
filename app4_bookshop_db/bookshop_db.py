""" Database backend for the bookshop app """

import sqlite3


def connect_to_db():
    """ Connect to a database

    Returns
    -------
    cursor: The cursor object

    """
    return sqlite3.connect("books.db").cursor()


def commit_and_close(db_conn):
    """ Commit the changes and close the db connection

    Arguments
    -------
    db_conn: the database connection
    """
    db_conn.commit()
    db_conn.close()


def create_book_db_table():
    """ Creates the book database table if doesn't exist """
    cur = connect_to_db()
    sql_str_create = "CREATE TABLE IF NOT EXISTS book "
    sql_str_params ="id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer"
    cur.execute(sql_str_create + "(" + sql_str_params + ")")
    commit_and_close(cur.connection)


def insert_book(title, author, year, isbn):
    """ insert a book in the database

    parameters
    ----------
    title : title of the book

    author : author of the book

    year : year of the book

    isbn : the isbn number of the book

    """
    cur = connect_to_db()
    sql_insert_str = "insert into book values (null,?,?,?,?)"
    cur.execute(sql_insert_str, (title, author, year, isbn))
    commit_and_close(cur.connection)


def get_db_rows():
    """ Get the Database rows

    Returns
    -------
    list: database rows

    """
    cur = connect_to_db()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    cur.connection.close()
    return rows


def search_book(title="", author="", year="", isbn=""):
    """ Search a book in the database

    Parameters
    ----------
    title : , optional

    author : , optional

    year : , optional

    isbn : , optional


    Returns
    -------
    list : database rows for te search result

    """
    cur = connect_to_db()
    sql_search_str1 = "SELECT * FROM book WHERE "
    sql_search_str2 = "title=? OR author=? OR year=? OR isbn=?"
    cur.execute(sql_search_str1 + sql_search_str2, (title, author, year, isbn))
    rows = cur.fetchall()
    cur.connection.close()
    return rows


def delete_db_entry(db_id):
    """ Deletes the database Entry

    Parameters
    ----------
    id : The id of the entry t be deleted

    """
    cur = connect_to_db()
    cur.execute("DELETE FROM book WHERE id=?", (db_id,))
    commit_and_close(cur.connection)


def update_db_entry(db_id, title, author, year, isbn):
    """ Update the database entry with given info

    Parameters
    ----------
    id : The id of the database entry

    title : Title of the book

    author : Author of the book

    year : Publication year

    isbn : ISBN number of the book

    """
    cur = connect_to_db()
    sql_update_str1 = "UPDATE book SET "
    sql_update_str2 = "title=?, author=?, year=?, isbn=? WHERE id=?"
    sql_update_str = sql_update_str1 + sql_update_str2
    cur.execute(sql_update_str, (title, author, year, isbn, db_id))
    commit_and_close(cur.connection)


def main():
    """ The main function to test the functionality """
    print("Testing the book app database")
    create_book_db_table()
    insert_book("The Sea", "John Tablet", 1918, 913123132)
    insert_book("The Sea", "John Senna", 1920, 91312333)
    insert_book("The Earth", "John Greme", 1922, 91312433)
    print(get_db_rows())
    print(search_book(author="John Tablet"))
    delete_db_entry(3)
    update_db_entry(2, "The Ocean", "John Tablet", 1918, 913123132)
    print(get_db_rows())


if __name__ == '__main__':
    main()
