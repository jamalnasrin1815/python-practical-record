# Student Grade Analyzer

marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / n

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Grade Analysis ---")
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)