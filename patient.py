from database.db import connect

def add_patient(name, age, gender, disease):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO patients(name, age, gender, disease) VALUES (?, ?, ?, ?)",
                (name, age, gender, disease))
    conn.commit()
    conn.close()

def view_patients():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    data = cur.fetchall()
    conn.close()
    return data