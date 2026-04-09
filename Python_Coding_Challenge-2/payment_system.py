# Taking number input
number = int(input("Enter a number: "))

# Checking if divisible by both 3 AND 5
if number % 3 == 0 and number % 5 == 0:
    print("Yes")
else:
    print("No")