import os
import cv2
import joblib

from insightface.app import FaceAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

DATASET_DIR = "dataset"
MODEL_DIR = "models"

os.makedirs(MODEL_DIR, exist_ok=True)

encodings = []
names = []

print("Loading InsightFace model...")

app = FaceAnalysis(
    providers=['CPUExecutionProvider']
)

app.prepare(ctx_id=0)

print("Training started...\n")

for person in os.listdir(DATASET_DIR):

    person_path = os.path.join(DATASET_DIR, person)

    if not os.path.isdir(person_path):
        continue

    print(f"Processing {person}")

    for image_name in os.listdir(person_path):

        image_path = os.path.join(person_path, image_name)

        try:
            img = cv2.imread(image_path)

            if img is None:
                print(f"Cannot read: {image_path}")
                continue

            faces = app.get(img)

            if len(faces) > 0:

                # Use first detected face
                embedding = faces[0].embedding

                encodings.append(embedding)
                names.append(person)

        except Exception as e:
            print(f"Error processing {image_path}")
            print(e)

if len(encodings) == 0:
    print("No faces found in dataset!")
    exit()

print("\nTraining classifier...")

encoder = LabelEncoder()

y = encoder.fit_transform(names)

model = KNeighborsClassifier(
    n_neighbors=1
)

model.fit(encodings, y)

joblib.dump(
    model,
    os.path.join(MODEL_DIR, "recognizer.pkl")
)

joblib.dump(
    encoder,
    os.path.join(MODEL_DIR, "encoder.pkl")
)

print("\nTraining completed successfully!")
print(f"Faces trained: {len(encodings)}")
print("Models saved in models/")