# Function to convert a list into a tuple
def convert_to_tuple(input_list):
    # tuple() constructor list ko tuple mein badal deta hai
    # Tuple immutable hota hai (change nahi ho sakta)
    return tuple(input_list)

# User se numbers input lena
user_data = input("Enter numbers separated by space: ")
# String ko list of integers mein badalna
my_list = [int(x) for x in user_data.split()]

# Output print karna
print(f"Output: {convert_to_tuple(my_list)}")