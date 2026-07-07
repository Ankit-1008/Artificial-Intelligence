import sqlite3
import os

# Create database folder if it doesn't exist
os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/attendance.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    time TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")