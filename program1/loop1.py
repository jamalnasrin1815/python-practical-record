#Simple Student Grade Analyzer
n = int(input("Enter number of subjects: "))
total = 0
for i in range(n):
 marks = int(input("Enter marks: "))
 total = total + marks
average = total / n
# Grade calculation
if average >= 75:
 grade = "A"
elif average >= 60:
 grade = "B"
elif average >= 50:
 grade = "C"
else:
 grade = "F"
print("Total =", total)
print("Average =", average)
print("Grade =", grade)
n = int(input("Enter number of subjects: "))
total = 0
i = 1
while i <= n:
 marks = int(input("Enter marks: "))
 total += marks
 i += 1
average = total / n
if average >= 60:
 grade = "Pass"
else:
 grade = "Fail"
print("Average =", average)
print("Grade =", grade)
n = int(input("Enter number of subjects: "))
marks = []
for i in range(n):
 m = int(input("Enter marks: "))
 marks.append(m)
total = sum(marks)
average = total / n
print("Marks:", marks)
print("Average:", average)
def calculate_grade(avg):
 if avg >= 75:
  return "A"
 elif avg >= 60:
  return "B"
 else:
  return "C"
n = int(input("Enter subjects: "))
total = 0
for i in range(n):
 total += int(input("Enter marks: "))
avg = total / n
print("Average:", avg)
print("Grade:", calculate_grade(avg))
marks = list(map(int, input("Enter marks separated by space: ").split()))
total = sum(marks)
avg = total / len(marks)
print("Average:", avg)