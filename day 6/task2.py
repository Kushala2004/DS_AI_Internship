import pandas as pd

names = pd.Series([
    "Kushala",
    "RAHUL",
    None,
    "Anjali",
    "PRIYA",
    None
])

print("Original Series:")
print(names)


print("\nMissing values:")
print(names.isna())

names = names.fillna("Unknown")

print("\nAfter filling missing values:")
print(names)

names = names.str.lower()

print("\nNames in lowercase:")
print(names)

result = names[names.str.contains("a")]

print("\nNames containing the letter 'a':")
print(result)