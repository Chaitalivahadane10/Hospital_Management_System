import streamlit as st
from modules.patient import add_patient, view_patients
from modules.doctor import add_doctor
from modules.appointment import book_appointment

st.title("🏥 Hospital Management System")

# 🔐 Initialize login state
if "login" not in st.session_state:
    st.session_state.login = False

# ---------- LOGIN SCREEN ----------
if not st.session_state.login:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "chaitalivahadane" and password == "chaitali10":
            st.session_state.login = True
            st.success("✅ Login successful!")
            st.rerun()  # <- updated from experimental_rerun
        else:
            st.error("❌ Incorrect username or password")

# ---------- MAIN APP ----------
else:
    st.write("✅ You are logged in!")

    # Logout button
    if st.button("Logout"):
        st.session_state.login = False
        st.rerun()  # <- updated from experimental_rerun

    # Sidebar Menu
    menu = ["Add Patient", "View Patients", "Add Doctor", "Book Appointment"]
    choice = st.sidebar.selectbox("Menu", menu)

    # ➤ Add Patient
    if choice == "Add Patient":
        st.subheader("Add Patient")
        name = st.text_input("Name")
        age = st.number_input("Age")
        gender = st.selectbox("Gender", ["Male", "Female"])
        disease = st.text_input("Disease")

        if st.button("Add Patient"):
            add_patient(name, age, gender, disease)
            st.success("Patient Added")

    # ➤ View Patients
    elif choice == "View Patients":
        st.subheader("Patient List")
        data = view_patients()
        st.write(data)

    # ➤ Add Doctor
    elif choice == "Add Doctor":
        st.subheader("Add Doctor")
        name = st.text_input("Doctor Name")
        specialization = st.text_input("Specialization")

        if st.button("Add Doctor"):
            add_doctor(name, specialization)
            st.success("Doctor Added")

    # ➤ Book Appointment
    elif choice == "Book Appointment":
        st.subheader("Book Appointment")
        patient_id = st.number_input("Patient ID")
        doctor_id = st.number_input("Doctor ID")
        date = st.date_input("Date")

        if st.button("Book"):
            book_appointment(patient_id, doctor_id, date)
            st.success("Appointment Booked")