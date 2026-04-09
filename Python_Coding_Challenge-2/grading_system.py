def get_grade(marks):
    # Standard grading logic (Example: 80-89 = B)
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# Input and Function Call
user_marks = int(input("Enter marks: "))
#printing output by using f string
print(f"Output: {get_grade(user_marks)}")