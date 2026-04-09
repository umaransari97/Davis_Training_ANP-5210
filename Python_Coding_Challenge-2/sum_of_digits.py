def sum_of_digits(num):
    total = 0
    
    while num > 0:
        total += num % 10
        num = num // 10
    
    return total

# Taking input from user
user_num = int(input("Enter a multi-digit number: "))

# Output
print(f"Output: {sum_of_digits(user_num)}")