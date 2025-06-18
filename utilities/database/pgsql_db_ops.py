# -*- coding: utf-8 -*-
"""
Module for interaction with PostgreSQL database.

Author:     Kushal Moolchandani
Created:    2025-02-28
"""

import pandas as pd
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import connection
from typing import Optional
from sqlalchemy import create_engine

#-------------------------------------------------------------------------------
def open_pg_connection(user: str,
                       password: str,
                       dbname: str, 
                       host: str = 'localhost', 
                       port: str = '5432') -> Optional[connection]:
    """ Creates a database connection to PostgreSQL database and returns a
    connection object.

    :Parameters:
        user: str
            username for database
        password: str
            password for database
        dbname: str
            name of database
        host: str
            host address for database
        port: str
            port number for database

    :Returns:
        conn: psycopg2.Connection
            connection to database
    """
    conn = None
    try:
        conn = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                port=port,
                                dbname=dbname)
        print(f'Connection open to {dbname}.')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    return conn

#-------------------------------------------------------------------------------
def close_pg_connection(conn: connection) -> None:
    """ Closes connection to PostgreSQL database specified by connection object.

    :Parameters:
        conn: psycopg2.extensions.connection
            connection to the database to be closed
    """
    conn.close()
    print(f'Connection closed.')

#-------------------------------------------------------------------------------
def execute_pgsql_command(conn: connection, 
                          sql_execute_string: str, 
                          params: Optional[tuple] = None) -> None:
    """ Executes SQL command passed as string argument on database. Needs 
    connection to database as an argument. Use this function to make changes 
    to database, with no return statement.

    :Parameters:
        conn: psycopg2.Connection
            connection to the database
        sql_execute_string: str
            SQL command
        params: tuple
            parameters for SQL command, optional
    """
    try:
        c = conn.cursor()
        if params:
            c.execute(sql.SQL(sql_execute_string).format(*(sql.Identifier(p) for p in params)))
        else:
            c.execute(sql_execute_string)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

#-------------------------------------------------------------------------------
def query_pgsql_table(conn: connection, 
                      sql_query_string: str) -> pd.DataFrame:
    """ Queries SQL table as per the passed command and returns data. Needs 
    connection to database as an argument. 

    :Parameters:
        conn: psycopg2.Connection
            connection to the database
        sql_query_string: str
            SQL command

    :Returns:
        df: pd.DataFrame
            data from query
    """
    try:
        df = pd.read_sql(sql_query_string, conn)  # type: ignore
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    return df

#-------------------------------------------------------------------------------
def upload_table(conn_string: str, table_loc: str, table_name: str) -> None:
    """
    Uploads table to PostgreSQL database.

    :Parameters:
        conn_string: str
            SQLAlchemy connection string (e.g., 'postgresql+psycopg2://user:password@host:port/dbname')
        table_loc: str
            location of table to be uploaded
        table_name: str
            name of table in database
    """
    try:
        df = pd.read_csv(table_loc)
        engine = create_engine(conn_string)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
    except Exception as error:
        print(error)


#===============================================================================
if __name__ == '__main__':
    pass