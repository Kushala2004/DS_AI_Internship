def total_marks(m1, m2, m3, m4, m5):
    return m1 + m2 + m3 + m4 + m5

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

result = total_marks(m1, m2, m3, m4, m5)
print("Total Marks =", result)