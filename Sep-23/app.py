import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import get_connection


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Student Management Dashboard",
    page_icon="🎓",
    layout="wide"
)


# ==========================================================
# APPLICATION TITLE
# ==========================================================

st.title("🎓 Student Management System")

st.subheader(
    "Student Attendance, Fee Payment and Marks Analysis"
)


# ==========================================================
# DATABASE FUNCTIONS
# ==========================================================


# ----------------------------------------------------------
# GET ALL STUDENTS
# ----------------------------------------------------------

def get_all_students():

    con = get_connection()

    query = """
        SELECT
            StudentId,
            StudentName
        FROM Student
        ORDER BY StudentId
    """

    df = pd.read_sql(
        query,
        con
    )

    con.close()

    return df


# ----------------------------------------------------------
# GET STUDENT DETAILS
# ----------------------------------------------------------

def get_student(student_id):

    con = get_connection()

    query = """
        SELECT *
        FROM Student
        WHERE StudentId = %s
    """

    df = pd.read_sql(
        query,
        con,
        params=(student_id,)
    )

    con.close()

    return df


# ----------------------------------------------------------
# GET ATTENDANCE
# ----------------------------------------------------------

def get_attendance(student_id):

    con = get_connection()

    query = """
        SELECT
            MonthName,
            TotalDays,
            PresentDays,
            ROUND(
                PresentDays * 100.0 / TotalDays,
                2
            ) AS AttendancePercentage

        FROM Attendance

        WHERE StudentId = %s

        ORDER BY AttendanceId
    """

    df = pd.read_sql(
        query,
        con,
        params=(student_id,)
    )

    con.close()

    return df


# ----------------------------------------------------------
# GET FEE DETAILS
# ----------------------------------------------------------

def get_fees(student_id):

    con = get_connection()

    query = """
        SELECT
            COALESCE(
                SUM(TotalFee),
                0
            ) AS TotalFee,

            COALESCE(
                SUM(PaidAmount),
                0
            ) AS PaidAmount,

            COALESCE(
                SUM(TotalFee - PaidAmount),
                0
            ) AS Balance

        FROM FeePayment

        WHERE StudentId = %s
    """

    df = pd.read_sql(
        query,
        con,
        params=(student_id,)
    )

    con.close()

    return df


# ----------------------------------------------------------
# GET MARKS
# ----------------------------------------------------------

def get_marks(student_id):

    con = get_connection()

    query = """
        SELECT
            Subject,
            InternalMarks,
            ExternalMarks,

            InternalMarks + ExternalMarks
            AS TotalMarks

        FROM Marks

        WHERE StudentId = %s

        ORDER BY MarkId
    """

    df = pd.read_sql(
        query,
        con,
        params=(student_id,)
    )

    con.close()

    return df


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🎓 Student Selection")


# Get all students

student_list = get_all_students()


# ----------------------------------------------------------
# CHECK STUDENT DATA
# ----------------------------------------------------------

if student_list.empty:

    st.error(
        "No students found in the Student table."
    )

    st.stop()


# ==========================================================
# CREATE DROPDOWN
# ==========================================================

student_options = (
    student_list["StudentId"].astype(str)
    + " - "
    + student_list["StudentName"]
).tolist()


selected_student = st.sidebar.selectbox(
    "Select Student",
    student_options
)


# ==========================================================
# GET SELECTED STUDENT ID
# ==========================================================

student_id = int(
    selected_student.split(" - ")[0]
)