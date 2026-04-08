from database.db import connect

def add_doctor(name, specialization):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO doctors(name, specialization) VALUES (?, ?)",
                (name, specialization))
    conn.commit()
    conn.close()