# Student Grade Calculator
# Beginner Python project for Codomax AI & ML Internship

def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


print("===== STUDENT GRADE CALCULATOR =====")

student_name = input("Enter student name: ")
number_of_subjects = int(input("Enter number of subjects: "))

marks = []

for subject_number in range(1, number_of_subjects + 1):
    while True:
        mark = float(input(f"Enter marks for subject {subject_number} (0-100): "))
        if 0 <= mark <= 100:
            marks.append(mark)
            break
        print("Invalid mark. Please enter a value from 0 to 100.")

total = sum(marks)
average = calculate_average(marks)
grade = calculate_grade(average)

print("\n===== RESULT =====")
print("Student Name:", student_name)
print("Total Marks:", total, "/", number_of_subjects * 100)
print("Average:", round(average, 2))
print("Grade:", grade)

if grade == "F":
    print("Result: Needs improvement")
else:
    print("Result: Pass")

print("==================")
