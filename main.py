# main.py - Student Grade Calculator

def calc_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"

marks = int(input("Enter your marks: "))
print("Your grade is:", calc_grade(marks))
Added main.py with core logic  (Fixes #2)
Updated README with usage instructions (Fixes #3)
Performed testing and fixed input bug (Fixes #4)
