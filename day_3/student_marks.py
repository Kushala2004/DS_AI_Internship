def get_marks():
    marks = []

    while True:
        mark = input("Enter mark (or type 'done' to finish): ")

        if mark.lower() == "done":
            break

        marks.append(float(mark))

    return marks


def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)


def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "A"
    elif 80 <= avg < 90:
        return "B"
    elif 70 <= avg < 80:
        return "C"
    elif 60 <= avg < 70:
        return "D"
    elif 50 <= avg < 60:
        return "E"
    else:
        return "F"


def display_result(name, marks, avg, grade):
    print("\n------ Student Report ------")
    print("Student Name :", name)
    print("Marks        :", marks)
    print("Average      :", round(avg, 2))
    print("Grade        :", grade)


def main():
    name = input("Enter student name: ")
    marks = get_marks()
    avg = calculate_average(marks)
    grade = calculate_grade(avg)
    display_result(name, marks, avg, grade)


# Run the program
main()