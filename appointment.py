from database.db import connect

def book_appointment(patient_id, doctor_id, date):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO appointments(patient_id, doctor_id, date) VALUES (?, ?, ?)",
                (patient_id, doctor_id, date))
    conn.commit()
    conn.close()