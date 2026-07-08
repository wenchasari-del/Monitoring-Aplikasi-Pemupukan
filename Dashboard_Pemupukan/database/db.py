import sqlite3
import pandas as pd

DB_NAME = "database/database.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pemupukan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tanggal TEXT,
        unit TEXT,
        blok TEXT,
        jenis_pupuk TEXT,
        jumlah_pupuk REAL,
        hk INTEGER,
        jenis_aplikasi TEXT
    )
    """)

    conn.commit()
    conn.close()


def tambah_data(data):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO pemupukan
    (tanggal,unit,blok,jenis_pupuk,jumlah_pupuk,hk,jenis_aplikasi)
    VALUES(?,?,?,?,?,?,?)
    """, data)

    conn.commit()
    conn.close()


def load_data():

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql(
        "SELECT * FROM pemupukan",
        conn
    )

    conn.close()

    return df