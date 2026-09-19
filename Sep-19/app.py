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
