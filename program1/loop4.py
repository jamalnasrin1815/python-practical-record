# Student Grade Analyzer with Pass/Fail

n = int(input("Enter number of subjects: "))

total = 0
failed = False

for i in range(n):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    total += mark

    if mark < 40:
        failed = True

average = total / n

if failed:
    result = "FAIL"
    grade = "F"
elif average >= 90:
    grade = "A+"
    result = "PASS"
elif average >= 80:
    grade = "A"
    result = "PASS"
elif average >= 70:
    grade = "B"
    result = "PASS"
elif average >= 60:
    grade = "C"
    result = "PASS"
elif average >= 50:
    grade = "D"
    result = "PASS"
else:
    grade = "F"
    result = "FAIL"

print("\n--- Student Grade Analyzer ---")
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
print("Result:", result)