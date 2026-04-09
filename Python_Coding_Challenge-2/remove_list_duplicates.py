# Function to remove duplicates from a list
def remove_duplicates(input_list):
    # Converting the list to a 'set' automatically removes duplicates
    # Then converting it back to a list
    unique_list = list(set(input_list))
    return unique_list

# Taking list input from user
user_input = input("Enter numbers separated by space: ")
# Converting the input string into a list of integers
data = [int(x) for x in user_input.split()]

# Calling function and printing result
print(f"Output: {remove_duplicates(data)}")