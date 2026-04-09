# Method to count numbers greater than 50
def count_high_values(numbers):
    count = 0
    for num in numbers:
        if num > 50:
            count += 1
    return count


#Function to take user input
def get_user_input():
    numbers = []
    n = int(input("How many numbers you want to enter: "))
    
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    return numbers


# Taking input from user
data_list = get_user_input()

# Calling main function
total_high = count_high_values(data_list)

# Output
print(f"Output: {total_high}")