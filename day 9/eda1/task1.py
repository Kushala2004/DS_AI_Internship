import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset
data = {
    "Name": ["Asha", "Rahul", "Priya", "Arjun", "Sneha",
             "Kiran", "Meena", "Ravi", "Anu", "Vijay"],

    "Study_Hours": [5, 3, 6, 2, 7, 4, 8, 3, 6, 2],

    "Attendance": [90, 75, 95, 60, 98, 80, 96, 70, 92, 65],

    "Marks": [85, 65, 90, 55, 95, 72, 98, 60, 88, 50]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Basic information
print("\nShape:")
print(df.shape)

print("\nStatistics:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Skewness
print("\nSkewness:")
print(df[["Study_Hours", "Attendance", "Marks"]].skew())

# Correlation
print("\nCorrelation:")
print(df[["Study_Hours", "Attendance", "Marks"]].corr())

# -------------------------------
# Visualizations
# -------------------------------

# 1. Marks Distribution
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

# 2. Study Hours vs Marks
plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# 3. Attendance vs Marks
plt.scatter(df["Attendance"], df["Marks"])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.show()

# 4. Boxplot for Outliers
sns.boxplot(x=df["Marks"])
plt.title("Marks Outlier Detection")
plt.show()

# 5. Correlation Heatmap
sns.heatmap(
    df[["Study_Hours", "Attendance", "Marks"]].corr(),
    annot=True
)
plt.title("Correlation Heatmap")
plt.show()

# Final observations
print("\nInsights:")
print("1. Students who study more hours generally score higher marks.")
print("2. Higher attendance is generally associated with higher marks.")
print("3. The boxplot helps identify possible outliers.")
print("4. Correlation shows the relationship between study hours, attendance and marks.")