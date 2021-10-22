import sqlite3
from sqlite3 import Error
from flask import g

def get_db():
    try:
        g.db = sqlite3.connect("baseDeDatos.db")
        return g.db
    except Error:
        print(Error)