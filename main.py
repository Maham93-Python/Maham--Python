name = input("Enter your name: ")
marks = float(input("Enter your marks: "))
if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print()
print("Student:", name)
print("Marks:", marks)
print("Grade:", grade)
