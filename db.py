import sqlite3

def connect():
    return sqlite3.connect("hospital.db")

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        disease TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS doctors(
        id INTEGER PRIMARY KEY,
        name TEXT,
        specialization TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointments(
        id INTEGER PRIMARY KEY,
        patient_id INTEGER,
        doctor_id INTEGER,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()