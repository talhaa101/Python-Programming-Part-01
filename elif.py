marks = input("please enter your marks = ")
marks = int(marks)

if marks >= 80:
    grade = "A+"

elif marks >= 70:
    grade = "B+"

elif marks >= 60:
    grade = "C+"

else:
    grade = "Fail"


print("Your grade is : ", grade)