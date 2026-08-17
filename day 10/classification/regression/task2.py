import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Read dataset
df = pd.read_csv("task2.csv")

print("Dataset:")
print(df)

# Input features
X = df[["Temperature", "Appliances", "Time_of_Day", "Previous_Usage"]]

# Target
y = df["Electricity_Consumption"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R2 Score:", r2)

# Predict for a new household
new_data = [[29, 7, 19, 16.7]]

prediction = model.predict(new_data)

print("\nNew Household:")
print("Temperature: 29")
print("Appliances: 7")
print("Time of Day: 19")
print("Previous Usage: 16.7")

print("\nPredicted Electricity Consumption:",
      prediction[0], "kWh")