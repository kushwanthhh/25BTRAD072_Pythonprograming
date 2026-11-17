students = {}
n = int(input("Enter number of students: "))


for i in range(n):
name = input("Enter student name: ") marks = float(input("Enter marks: ")) students[name] = marks

print("\nStudent Results")


for name, marks in students.items(): if marks >= 90:
grade = "A"
 
elif marks >= 75:
grade = "B"
elif marks >= 50:
grade = "C" elif marks >= 35:
grade = "D" else:
grade = "Fail"


print(name, "-", marks, "-", grade)
