from pandas import DataFrame
import pandas.io.sql as sqlio
from psycopg2 import connect, Error
from tkinter.messagebox import showerror

def open_connection():
    """Connect to database"""
    connection = None
    try:
        connection = connect(
        host="postgres",
        port="5432",
        database="gres",
        user="gres",
        password="gres")
    except Error as er:
        showerror(title="Fatal error", message=f"Connection failed {er}")
        
    return connection

def close_connection(connection):
    """Close connection"""
    connection.close()

def get_data(sql_query: str) -> DataFrame:
    connection = open_connection()
    if connection == None:
        raise SystemExit

    data = sqlio.read_sql_query(sql_query, connection)
    close_connection(connection)
    return data
