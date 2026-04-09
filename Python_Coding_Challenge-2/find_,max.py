def find_max_manual(number_list):
    # Assuming the first number in the list is the largest
    max_val = number_list[0]
    # Looping through the rest of the list
    for val in number_list:
        # If the current value is bigger than our current max_val
        if val > max_val:
            # Update max_val with the new bigger value
            max_val = val
    
    return max_val # Returning the largest value found

# Taking input as a string and converting to a list of integers
user_input = input("Enter numbers separated by space: ")
# Splitting the string and converting each item to int
numbers = [int(x) for x in user_input.split()]

# Calling the function manually to find the maximum
print(f"Output: {find_max_manual(numbers)}")