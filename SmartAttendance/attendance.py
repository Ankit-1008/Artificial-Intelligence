import cv2
import joblib
import sqlite3
import pandas as pd
import os

from datetime import datetime
from insightface.app import FaceAnalysis

MODEL_PATH = "models/recognizer.pkl"
ENCODER_PATH = "models/encoder.pkl"

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

# Initialize InsightFace
app = FaceAnalysis(providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0)

os.makedirs("attendance", exist_ok=True)

csv_file = "attendance/attendance.csv"

if not os.path.exists(csv_file):
    pd.DataFrame(
        columns=["Name", "Date", "Time"]
    ).to_csv(csv_file, index=False)

marked = set()

cap = cv2.VideoCapture(0)

print("Attendance Started")
print("Press q to quit")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    faces = app.get(frame)

    for face in faces:

        embedding = face.embedding

        pred = model.predict([embedding])

        name = encoder.inverse_transform(pred)[0]

        bbox = face.bbox.astype(int)

        x1, y1, x2, y2 = bbox

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            name,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        if name not in marked:

            now = datetime.now()

            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")

            conn = sqlite3.connect(
                "database/attendance.db"
            )

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO attendance
                (name,date,time)
                VALUES(?,?,?)
                """,
                (name, date, time)
            )

            conn.commit()
            conn.close()

            df = pd.DataFrame(
                [[name, date, time]],
                columns=["Name", "Date", "Time"]
            )

            df.to_csv(
                csv_file,
                mode="a",
                header=False,
                index=False
            )

            marked.add(name)

            print(f"{name} Marked Present")

    cv2.imshow(
        "Smart Attendance",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()