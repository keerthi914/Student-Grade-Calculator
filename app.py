import streamlit as st

st.title("Student Grade Calculator")

name = st.text_input("Student Name")
roll_no = st.text_input("Roll Number")

m1 = st.number_input("Subject 1 Marks", 0, 100)
m2 = st.number_input("Subject 2 Marks", 0, 100)
m3 = st.number_input("Subject 3 Marks", 0, 100)
m4 = st.number_input("Subject 4 Marks", 0, 100)
m5 = st.number_input("Subject 5 Marks", 0, 100)

if st.button("Calculate"):
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 35:
        grade = "D"
    else:
        grade = "F"

    st.write("### Student Report")
    st.write("Name:", name)
    st.write("Roll Number:", roll_no)
    st.write("Total:", total)
    st.write("Average:", average)
    st.write("Grade:", grade)
