import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect():
    conn = sqlite3.connect('data.db')
    return conn


def connect_row_factory():
    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    return conn
