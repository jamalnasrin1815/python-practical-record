# Complete Student Grade Analyzer

name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

total = 0

print("\nEnter subject details:")

for i in range(n):
    subject = input(f"\nEnter subject {i + 1} name: ")
    mark = float(input(f"Enter marks in {subject}: "))

    total += mark

    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"{subject}: {mark} - Grade {grade}")

average = total / n

if average >= 90:
    overall_grade = "A+"
elif average >= 80:
    overall_grade = "A"
elif average >= 70:
    overall_grade = "B"
elif average >= 60:
    overall_grade = "C"
elif average >= 50:
    overall_grade = "D"
else:
    overall_grade = "F"

print("\n==============================")
print("       GRADE ANALYZER")
print("==============================")
print("Student Name :", name)
print("Total Marks  :", total)
print("Average      :", round(average, 2))
print("Overall Grade:", overall_grade)
print("==============================")