import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load Dataset
df = pd.read_csv("data/student_performance_dataset.csv")

# Create Pass/Fail Target
df["Pass_Fail"] = (df["exam_score"] >= 40).astype(int)

# Drop target column
X = df.drop(["exam_score", "Pass_Fail"], axis=1)
y = df["Pass_Fail"]

# Convert categorical columns
X = pd.get_dummies(X, drop_first=True)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")

# Save Model
joblib.dump(model, "models/random_forest.pkl")

# Save Column Names
joblib.dump(X.columns.tolist(), "models/columns.pkl")

print("Model Saved Successfully")