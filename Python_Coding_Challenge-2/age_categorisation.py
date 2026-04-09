# Taking age input
age = int(input("Enter age: "))

# Checking age groups using if-elif-else
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")