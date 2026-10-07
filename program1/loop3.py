# Subject-wise Grade Analyzer

n = int(input("Enter number of subjects: "))

total = 0

for i in range(n):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
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

    print(f"Subject {i + 1}: {mark} -> Grade {grade}")

average = total / n

print("\nTotal Marks:", total)
print("Average Marks:", round(average, 2))