# -*- coding: utf-8 -*-
"""
Module for interaction with SQLite database files.

Author:     Kushal Moolchandani
Created:    2025-02-06
"""

import pandas
import sqlite3
import sys

#-------------------------------------------------------------------------------
def connect_sqlite_db(db_file: str, 
                      db_loc: str) -> sqlite3.Connection:
    """ Creates a database connection to SQLite database and returns a 
    connection object.
    
    Inputs:
        db_loc: path to database
        db_file: name of database file
    
    Outputs:
        conn: connection to database (return)
    """
    conn = None
    try:
        conn = sqlite3.connect(''.join([db_loc,'/',db_file]))
        print(f'Connection open to {db_file}.')
    except sqlite3.Error as e:
        print(e)
    
    return conn

#-------------------------------------------------------------------------------
def disconnect_sqlite_db(conn: sqlite3.Connection) -> None:
    """ Closes connection to SQLite database specified by connection object.

    Inputs:
        conn: connection to the database to be closed
    """
    conn.close()
    print('Connection closed.')

#-------------------------------------------------------------------------------
def execute_sql_command(conn: sqlite3.Connection, 
                        sql_execute_string: str) -> None:
    """ Executes SQL command passed as string argument on database. Needs 
    connection to database as an argument. Use this function to make changes 
    to database, with no return statement.
    
    Inputs:
        conn: connection to the database
        sql_execute_string: SQL command
    """
    try:
        c = conn.cursor()
        c.execute(sql_execute_string)
    except sqlite3.Error as e:
        print(e)

#-------------------------------------------------------------------------------
def query_sql_command(conn: sqlite3.Connection, 
                      sql_query_string: str):
    """ Queries SQL table as per the passed command and returns data. Needs 
    connection to database as an argument. 
    
    Inputs:
        conn: connection to the database
        sql_query_string: SQL command
    
    Outputs:
        result: data returned from database
    """
    try:
        c = conn.cursor()
        c.execute(sql_query_string)

        rows = c.fetchall()
    except sqlite3.Error as e:
        print(e)
    
    return rows

#-------------------------------------------------------------------------------
def upload_table(conn: sqlite3.Connection, 
                 table_loc: str, 
                 table_name: str):
    """
    Uploads data table to specified database.

    Inputs:
        conn: connection to a database
        table_loc: full path to data table
        table_name: name of table in the database
    """

    c = conn.cursor()
    data = pandas.read_csv(table_loc)
    data.to_sql(table_name, conn, if_exists='replace',
                    index = False, chunksize = 10000)
    
#===============================================================================
if __name__ == '__main__':
    try:
        conn = connect_sqlite_db(sys.argv[0], sys.argv[1])
    except IndexError:
        print(f'Could not establish connection to database. Please check input arguments and try again.')
    disconnect_sqlite_db(conn)
