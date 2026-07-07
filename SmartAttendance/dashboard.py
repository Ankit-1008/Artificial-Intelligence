import streamlit as st
import sqlite3
import pandas as pd

st.title("Smart Attendance Dashboard")

conn = sqlite3.connect(
    "database/attendance.db"
)

query = """
SELECT *
FROM attendance
ORDER BY id DESC
"""

df = pd.read_sql_query(
    query,
    conn
)

conn.close()

st.subheader("Attendance Records")

st.dataframe(
    df,
    use_container_width=True
)

st.subheader("Statistics")

st.metric(
    "Total Entries",
    len(df)
)

if not df.empty:

    students = df["name"].nunique()

    st.metric(
        "Unique Students",
        students
    )