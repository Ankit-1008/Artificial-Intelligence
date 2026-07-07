import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/random_forest.pkl")
columns = joblib.load("models/columns.pkl")

st.title("Student Performance Predictor")

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0
)

exercise_minutes = st.number_input(
    "Exercise Minutes",
    min_value=0
)

focus_index = st.number_input(
    "Focus Index",
    min_value=0
)

if st.button("Predict"):

    sample = pd.DataFrame(
        0,
        index=[0],
        columns=columns
    )

    if "study_hours" in sample.columns:
        sample["study_hours"] = study_hours

    if "sleep_hours" in sample.columns:
        sample["sleep_hours"] = sleep_hours

    if "exercise_minutes" in sample.columns:
        sample["exercise_minutes"] = exercise_minutes

    if "focus_index" in sample.columns:
        sample["focus_index"] = focus_index

    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.success("PASS")
    else:
        st.error("FAIL")