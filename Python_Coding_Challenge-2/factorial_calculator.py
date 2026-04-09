#method for calculatng factorial
def factorial_calculator(n):
    fact =1
    for i in range(1,n+1):
       fact= fact * i;
    return fact;

#taking user input
num= int(input("Enter a number:"))

#printing and callling method for calucating factorial
print(f"Factorial of {num} is {factorial_calculator(num)}")