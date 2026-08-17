import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Read dataset
df = pd.read_csv("task1.csv")

print("Dataset:")
print(df)

# Convert Result into numbers
df["Result"] = df["Result"].map({"Fail": 0, "Pass": 1})

# Input
X = df[["Study_Hours", "Attendance", "Assignment_Score"]]

# Output
y = df["Result"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# Predict a new student
new_student = [[5, 80, 65]]

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")