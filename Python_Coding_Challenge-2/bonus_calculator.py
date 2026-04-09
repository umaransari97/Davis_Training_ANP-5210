#Python code for bonus calculator
def bonus_calculator(salary):
    return salary * 0.07

#taking input from user
salary = int(input("Enter your salary:"))
print(f"Bonus amount :{bonus_calculator(salary)}")
