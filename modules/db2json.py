import sqlite3
from .configs import Config_Read

def databaseQueries():
    config = Config_Read()
    con = sqlite3.connect(config['DEFAULT']['database_path'], check_same_thread=False)
    cur = con.cursor()

    data = {}

    card = con.execute("SELECT * FROM card")

