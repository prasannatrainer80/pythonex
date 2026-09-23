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


marks_df = get_marks(
    student_id
)


# ==========================================================
# GET SELECTED STUDENT ID
# ==========================================================

student_id = int(
    selected_student.split(" - ")[0]
)

# ==========================================================
# LOAD STUDENT DATA
# ==========================================================

student_df = get_student(
    student_id
)

fee_df = get_fees(
    student_id
)
# ==========================================================
# CHECK STUDENT
# ==========================================================

if student_df.empty:

    st.error(
        "Student details not found."
    )

    st.stop()


# Convert first row into dictionary

student = student_df.iloc[0]


# ==========================================================
# STUDENT INFORMATION
# ==========================================================

st.header("👨‍🎓 Student Information")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.write("**Student ID**")

    st.info(
        student["StudentId"]
    )


with col2:

    st.write("**Student Name**")

    st.info(
        student["StudentName"]
    )


with col3:

    st.write("**Course**")

    st.info(
        student["Course"]
    )


with col4:

    st.write("**Year**")

    st.info(
        student["Year"]
    )


# ----------------------------------------------------------
# SECOND ROW
# ----------------------------------------------------------

col1, col2, col3 = st.columns(3)


with col1:

    st.write("**Gender**")

    st.info(
        student["Gender"]
    )


with col2:

    st.write("**Email**")

    st.info(
        student["Email"]
    )


with col3:

    st.write("**Phone**")

    st.info(
        student["Phone"]
    )


st.divider()

attendance_df = get_attendance(
    student_id
)

# ==========================================================
# FEE ANALYSIS
# ==========================================================

if not fee_df.empty:

    total_fee = float(
        fee_df[
            "TotalFee"
        ].iloc[0]
    )

    paid_fee = float(
        fee_df[
            "PaidAmount"
        ].iloc[0]
    )

    balance_fee = float(
        fee_df[
            "Balance"
        ].iloc[0]
    )

else:

    total_fee = 0

    paid_fee = 0

    balance_fee = 0



# ==========================================================
# ATTENDANCE ANALYSIS
# ==========================================================

if not attendance_df.empty:

    total_days = attendance_df[
        "TotalDays"
    ].sum()

    present_days = attendance_df[
        "PresentDays"
    ].sum()

    absent_days = (
        total_days
        -
        present_days
    )

    attendance_percentage = round(
        present_days
        /
        total_days
        *
        100,
        2
    )

else:

    total_days = 0

    present_days = 0

    absent_days = 0

    attendance_percentage = 0

# ==========================================================
# MARKS ANALYSIS
# ==========================================================

if not marks_df.empty:

    total_marks = int(
        marks_df[
            "TotalMarks"
        ].sum()
    )

    average_marks = round(
        marks_df[
            "TotalMarks"
        ].mean(),
        2
    )

    highest_marks = int(
        marks_df[
            "TotalMarks"
        ].max()
    )

    lowest_marks = int(
        marks_df[
            "TotalMarks"
        ].min()
    )

else:

    total_marks = 0

    average_marks = 0

    highest_marks = 0

    lowest_marks = 0


# ==========================================================
# DASHBOARD KPI CARDS
# ==========================================================

st.header("📊 Student Dashboard")


col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "Attendance",
        f"{attendance_percentage}%"
    )


with col2:

    st.metric(
        "Present Days",
        present_days
    )


with col3:

    st.metric(
        "Total Marks",
        total_marks
    )


with col4:

    st.metric(
        "Average Marks",
        average_marks
    )


with col5:

    st.metric(
        "Fee Balance",
        f"₹{balance_fee:,.2f}"
    )


st.divider()


# ==========================================================
# ATTENDANCE SECTION
# ==========================================================

st.header("📅 Attendance Analysis")


col1, col2 = st.columns(2)


# ----------------------------------------------------------
# ATTENDANCE CHART
# ----------------------------------------------------------

with col1:

    if not attendance_df.empty:

        fig, ax = plt.subplots()

        ax.plot(
            attendance_df["MonthName"],
            attendance_df[
                "AttendancePercentage"
            ],
            marker="o"
        )

        ax.set_title(
            "Monthly Attendance"
        )

        ax.set_xlabel(
            "Month"
        )

        ax.set_ylabel(
            "Attendance %"
        )

        ax.set_ylim(
            0,
            100
        )

        ax.grid(
            True
        )

        plt.xticks(
            rotation=30
        )

        st.pyplot(
            fig
        )

    else:

        st.warning(
            "Attendance data not available."
        )


# ----------------------------------------------------------
# ATTENDANCE SUMMARY
# ----------------------------------------------------------

with col2:

    st.subheader(
        "Attendance Summary"
    )

    st.metric(
        "Total Working Days",
        total_days
    )

    st.metric(
        "Present Days",
        present_days
    )

    st.metric(
        "Absent Days",
        absent_days
    )

    st.metric(
        "Attendance %",
        f"{attendance_percentage}%"
    )


# ==========================================================
# ATTENDANCE TABLE
# ==========================================================

st.subheader(
    "Monthly Attendance Details"
)


if not attendance_df.empty:

    st.dataframe(
        attendance_df,
        use_container_width=True,
        hide_index=True
    )


st.divider()

# ==========================================================
# MARKS ANALYSIS
# ==========================================================

st.header("📚 Marks Analysis")


col1, col2 = st.columns(2)


# ----------------------------------------------------------
# SUBJECT-WISE MARKS
# ----------------------------------------------------------

with col1:

    if not marks_df.empty:

        fig, ax = plt.subplots()

        ax.bar(
            marks_df["Subject"],
            marks_df["TotalMarks"]
        )

        ax.set_title(
            "Subject-wise Total Marks"
        )

        ax.set_xlabel(
            "Subject"
        )

        ax.set_ylabel(
            "Total Marks"
        )

        plt.xticks(
            rotation=30
        )

        st.pyplot(
            fig
        )

    else:

        st.warning(
            "Marks data not available."
        )


# ----------------------------------------------------------
# MARKS SUMMARY
# ----------------------------------------------------------

with col2:

    st.subheader(
        "Marks Summary"
    )

    st.metric(
        "Total Marks",
        total_marks
    )

    st.metric(
        "Average Marks",
        average_marks
    )

    st.metric(
        "Highest Marks",
        highest_marks
    )

    st.metric(
        "Lowest Marks",
        lowest_marks
    )


# ==========================================================
# INTERNAL VS EXTERNAL
# ==========================================================

st.subheader(
    "📖 Internal vs External Marks"
)


if not marks_df.empty:

    fig, ax = plt.subplots()

    x = range(
        len(marks_df)
    )

    width = 0.35


    ax.bar(
        [
            i - width / 2
            for i in x
        ],

        marks_df[
            "InternalMarks"
        ],

        width,

        label="Internal"
    )


    ax.bar(
        [
            i + width / 2
            for i in x
        ],

        marks_df[
            "ExternalMarks"
        ],

        width,

        label="External"
    )


    ax.set_xticks(
        list(x)
    )

    ax.set_xticklabels(
        marks_df["Subject"],
        rotation=30
    )

    ax.set_ylabel(
        "Marks"
    )

    ax.set_title(
        "Internal vs External Marks"
    )

    ax.legend()

    st.pyplot(
        fig
    )


# ==========================================================
# MARKS TABLE
# ==========================================================

st.subheader(
    "Subject-wise Marks Details"
)


if not marks_df.empty:

    st.dataframe(
        marks_df,
        use_container_width=True,
        hide_index=True
    )


st.divider()


# ==========================================================
# FEE ANALYSIS
# ==========================================================

st.header("💰 Fee Payment Analysis")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Total Fee",
        f"₹{total_fee:,.2f}"
    )


with col2:

    st.metric(
        "Paid Amount",
        f"₹{paid_fee:,.2f}"
    )


with col3:

    st.metric(
        "Balance",
        f"₹{balance_fee:,.2f}"
    )


# ----------------------------------------------------------
# FEE PIE CHART
# ----------------------------------------------------------

if total_fee > 0:

    fig, ax = plt.subplots()

    values = [
        paid_fee,
        balance_fee
    ]

    labels = [
        "Paid",
        "Balance"
    ]

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Fee Payment Status"
    )

    st.pyplot(
        fig
    )


st.divider()


# ==========================================================
# PERFORMANCE ANALYSIS
# ==========================================================

st.header("📈 Overall Performance Analysis")


col1, col2, col3 = st.columns(3)


# ----------------------------------------------------------
# ATTENDANCE STATUS
# ----------------------------------------------------------

with col1:

    st.subheader(
        "Attendance Status"
    )

    if attendance_percentage >= 75:

        st.success(
            "Attendance is above 75%"
        )

    else:

        st.warning(
            "Attendance is below 75%"
        )


# ----------------------------------------------------------
# ACADEMIC STATUS
# ----------------------------------------------------------

with col2:

    st.subheader(
        "Academic Status"
    )

    if average_marks >= 75:

        st.success(
            "Good Academic Performance"
        )

    elif average_marks >= 50:

        st.warning(
            "Average Academic Performance"
        )

    else:

        st.error(
            "Needs Improvement"
        )


# ----------------------------------------------------------
# FEE STATUS
# ----------------------------------------------------------

with col3:

    st.subheader(
        "Fee Status"
    )

    if balance_fee == 0:

        st.success(
            "Fee Fully Paid"
        )

    else:

        st.warning(
            f"Fee Balance: ₹{balance_fee:,.2f}"
        )


st.divider()


# ==========================================================
# FOOTER
# ==========================================================

st.caption(
    "Student Management System | "
    "Python + Streamlit + MySQL + Pandas + Matplotlib"
)
