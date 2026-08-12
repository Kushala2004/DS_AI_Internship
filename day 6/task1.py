import pandas as pd
marks = pd.Series(
    [75, 55, 85, 62, 45],
    index=["Maths", "Python", "Science", "English", "Computer"]
)

print("Student Marks:")
print(marks)
print("\nMark at position 0:", marks.iloc[0])
print("Mark at position 2:", marks.iloc[2])
print("\nMaths mark:", marks["Maths"])
print("Science mark:", marks["Science"])
print("\nValues:")
print(marks.values)
print("\nIndex:")
print(marks.index)
print("\nMarks above 60:")
print(marks[marks > 60])