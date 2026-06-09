import sqlite3

conn = sqlite3.connect("db/example.db")

def run_sql(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()