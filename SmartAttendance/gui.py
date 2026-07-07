import tkinter as tk
from tkinter import messagebox
import subprocess

root = tk.Tk()

root.title("Smart Attendance System")
root.geometry("400x300")

title = tk.Label(
    root,
    text="Smart Attendance",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)


def register_student():
    subprocess.run(
        ["python", "register_student.py"]
    )


def train_model():
    subprocess.run(
        ["python", "train.py"]
    )

    messagebox.showinfo(
        "Success",
        "Training Completed"
    )


def start_attendance():
    subprocess.run(
        ["python", "attendance.py"]
    )


def open_dashboard():
    subprocess.run(
        ["streamlit", "run", "dashboard.py"]
    )


btn1 = tk.Button(
    root,
    text="Register Student",
    width=25,
    command=register_student
)

btn1.pack(pady=10)

btn2 = tk.Button(
    root,
    text="Train Model",
    width=25,
    command=train_model
)

btn2.pack(pady=10)

btn3 = tk.Button(
    root,
    text="Start Attendance",
    width=25,
    command=start_attendance
)

btn3.pack(pady=10)

btn4 = tk.Button(
    root,
    text="Dashboard",
    width=25,
    command=open_dashboard
)

btn4.pack(pady=10)

root.mainloop()