import joblib

obj = joblib.load("models/recognizer.pkl")

print(type(obj))
print(obj)