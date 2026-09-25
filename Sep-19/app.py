import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import get_connection


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Employee Dashboard",
    page_icon="📊",
    layout="wide"
)


# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("📊 Employee Data Analysis Dashboard")

st.write(
    "Python + MySQL + SQL + Pandas + Matplotlib + Streamlit"
)


# -------------------------------------------------
# Load Data From MySQL
# -------------------------------------------------

connection = get_connection()

query = """
SELECT
    empno,
    name,
    gender,
    dept,
    desig,
    basic
FROM employees
"""

df = pd.read_sql(query, connection)

connection.close()


# -------------------------------------------------
# Sidebar
# -------------------------------------------------

st.sidebar.header("Dashboard Filters")

departments = ["All"] + sorted(
    df["dept"].unique().tolist()
)

selected_department = st.sidebar.selectbox(
    "Select Department",
    departments
)


# -------------------------------------------------
# Filter Data
# -------------------------------------------------

if selected_department == "All":

    filtered_df = df

else:

    filtered_df = df[
        df["dept"] == selected_department
    ]


# -------------------------------------------------
# KPI Calculations
# -------------------------------------------------

total_employees = len(filtered_df)

average_salary = filtered_df["basic"].mean()

maximum_salary = filtered_df["basic"].max()

minimum_salary = filtered_df["basic"].min()


# -------------------------------------------------
# KPI Display
# -------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Employees",
    total_employees
)

col2.metric(
    "Average Salary",
    f"₹{average_salary:,.0f}"
)

col3.metric(
    "Highest Salary",
    f"₹{maximum_salary:,.0f}"
)

col4.metric(
    "Lowest Salary",
    f"₹{minimum_salary:,.0f}"
)


st.divider()


# -------------------------------------------------
# Department Employee Count
# -------------------------------------------------

st.subheader("👥 Department-wise Employee Count")

dept_count = (
    filtered_df
    .groupby("dept")
    .size()
    .reset_index(name="Employee_Count")
)

fig1, ax1 = plt.subplots()

ax1.bar(
    dept_count["dept"],
    dept_count["Employee_Count"]
)

ax1.set_xlabel("Department")

ax1.set_ylabel("Number of Employees")

ax1.set_title(
    "Employees by Department"
)

st.pyplot(fig1)


# -------------------------------------------------
# Department Average Salary
# -------------------------------------------------

st.subheader("💰 Department-wise Average Salary")

dept_salary = (
    filtered_df
    .groupby("dept")["basic"]
    .mean()
    .reset_index()
)

fig2, ax2 = plt.subplots()

ax2.bar(
    dept_salary["dept"],
    dept_salary["basic"]
)

ax2.set_xlabel("Department")

ax2.set_ylabel("Average Salary")

ax2.set_title(
    "Average Salary by Department"
)

st.pyplot(fig2)


# -------------------------------------------------
# Employee Table
# -------------------------------------------------

st.subheader("📋 Employee Details")

st.dataframe(
    filtered_df,
    use_container_width=True
)